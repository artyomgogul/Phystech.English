WORDS = {'elem_en-ru':{}, 'elem_ru-en':{}, 'elem_rand':{}, 'inter_en-ru':{}, 'inter_ru-en':{}, 'inter_rand':{},
         'upper_en-ru':{}, 'upper_ru-en':{}, 'upper_rand':{}}

def data_words(level):
	with open(f'C:/Users/Human/PycharmProjects/TelegramBot/words/{level}.txt', 'r') as f:
		for line in f:
			WORDS[f'{level}_en-ru'].update({line[:line.index(':')].strip(): line[line.index(':') + 1:].strip()})
			WORDS[f'{level}_ru-en'].update({line[line.index(':') + 1:].strip(): line[:line.index(':')].strip()})

	WORDS[f'{level}_rand'].update(WORDS[f'{level}_en-ru'])
	WORDS[f'{level}_rand'].update(WORDS[f'{level}_ru-en'])

data_words('elem')
data_words('inter')
data_words('upper')