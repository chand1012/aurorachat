HELP_MESSAGE = ''' # Hello! I'm Aurora, your Discord AI assistant

Here is everything I can do!

## Chat
- `/chat <prompt> <attachment>`: Chat with me! Both prompt and attachment are optional.
    - This starts a thread with me, and you (or anyone else) can continue chatting with me there! I can even parse attachments!
- `/cancel`: Cancels the most recent request you made to me.
- `/close`: Close the thread you're in with me.
- `/delete`: Delete the thread you're in with me.
 

## Images
- `/imagine <prompt> <quality>`: Have me draw for you! Prompt is required, quality is optional.
Quality can be one of `normal`, `best`, or `best - uncensored`. Default is `normal`.

## Summaries
- I automatically summarize YouTube videos! Just paste a link to a video, and if there is a summary available I'll react with 📖. Click the reaction to see the summary!

## Speak
- `/speak <prompt> <speed>`: Have me read text to you! Prompt is required. Default speed is 0.9.

## Ping
- `/ping`: Pong!

## Help
- `/help`: Show this message.
'''

long_descriptions = {
    'chat': '''Chat with me! Both prompt and attachment are optional. This starts a thread with me, and you (or anyone else) can continue chatting with me there! I can even parse attachments!''',
    'cancel': '''Cancels the most recent request you made to me.''',
    'close': '''Close the thread you're in with me. Does not delete the thread, and does nothing if you're not in a thread with me.''',
    'delete': '''Delete the thread you're in with me. Does nothing if you're not in a thread with me.''',
    'imagine': '''Have me draw for you! Prompt is required, quality is optional. Quality can be one of `normal`, `best`, or `best - uncensored`. Default is `normal`.''',
    'speak': '''Have me read text to you! Prompt is required. Default speed is 0.9.''',
    'ping': '''Pong!''',
}
