from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required

from .models import Messages
from .forms import ConversationMessageForm

# Create your views here.
@login_required
def new_message(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('inbox:details', pk=item_pk)
    
    conversations = Messages.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        return redirect('messaging:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Messages.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('item:details', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'inbox/new.html', {
        'form':form
        
    })

@login_required
def inbox(request):
    conversations = Messages.objects.filter(members__in=[request.user.id])
    return render(request, 'inbox/inbox.html', {
        'conversations': conversations
    })
    

@login_required
def detail(request, pk):
    conversation = Messages.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()

            return redirect('messaging:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'inbox/detail.html', {
        'conversation': conversation,
        'form': form,
    })
