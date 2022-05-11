WORDS = {'eleme_en-ru':{}, 'eleme_ru-en':{}, 'eleme_rndom':{}, 'inter_en-ru':{}, 'inter_ru-en':{}, 'inter_rndom':{},
         'upper_en-ru':{}, 'upper_ru-en':{}, 'upper_rndom':{}, 'prein_en-ru':{}, 'prein_ru-en':{}, 'prein_rndom':{}}

def data_words(level):
	with open(f'C:/Users/Human/PycharmProjects/TelegramBot/words/{level}.txt', 'r') as f:
		for line in f:
			WORDS[f'{level}_en-ru'].update({line[:line.index(':')].strip(): line[line.index(':') + 1:].strip()})
			WORDS[f'{level}_ru-en'].update({line[line.index(':') + 1:].strip(): line[:line.index(':')].strip()})

	WORDS[f'{level}_rndom'].update(WORDS[f'{level}_en-ru'])
	WORDS[f'{level}_rndom'].update(WORDS[f'{level}_ru-en'])

data_words('eleme')
data_words('inter')
data_words('prein')
data_words('upper')
