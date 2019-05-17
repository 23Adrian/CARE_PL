from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from Dependency import care_parse
from prompt_toolkit.formatted_text import HTML


care_completer = WordCompleter(['has', 'diagnose', 'remove', 'create', 'queue', 'attend', 'help',
                                'symptoms', 'sneezing', 'sore_throat', 'congestion', 'coughing',
                                'low_fever', 'fever', 'high_fever', 'aches', 'chills', 'fatigue',
                                'headache', 'severe_headache', 'nausea', 'skin_rash', 'joint_pain',
                                'malaise', 'vomiting', 'diarrhea', 'muscle_pain', 'dizziness',
                                'numb_extremities', 'confusion', 'frequent_urination', 'weight_loss',
                                'constant_tiredness', '()', 'list'], ignore_case=True)


def bottom_toolbar():
    return HTML('Command <b><style bg="ansired">Help</style></b> to seek help ------'
                ' Command <b><style bg="ansired">Exit</style></b> to exit')


style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


def main():
    session = PromptSession(completer=care_completer, style=style, complete_while_typing=True,
                            bottom_toolbar=bottom_toolbar())
    print("\n\n\n\n\n")
    while True:
        try:
            text = session.prompt('\nCARE >> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            care_parse.do_parse(text)
    print('Exiting CARE...')


if __name__ == '__main__':
    main()
