# -*- coding: utf-8 -*-

import os
import re

#contengan = ['gratis']
#no_contengan = ['niños']
contengan = ['mapa', 'zoo', 'calle', 'alquiler', 'teatro', 'cine', 'atraccion','precio', 'pueblo', 'atracción',
          'plano', 'llegar', 'rio', 'warner', 'pelicula', 'callejero', 'tren', 'horario', 'renfe', 'alvia',
          'ave', 'estación', 'estacion', 'convento', 'museo', 'tarifa', 'ikea', 'android', 'video', 'fotocasa', 'ver']
no_contengan = ['hotel', 'motel', 'apartamento', 'host', 'inn', 'parador', 'resort', 'lodging', 'alojamiento',
             'appartment', 'apartment', 'guest', 'bungalow', 'hostel', 'hostal', 'hacienda', 'aparthotel',
             'apartahotel', 'hospedería', 'ibis', 'nh', 'melia', 'habitacion', 'habitación', 'vacacional',
             'vacacion', 'guest']
for kwd in enumerate(contengan):
    contengan[kwd[0]] = kwd[1].rstrip('s').rstrip('a').rstrip('e').rstrip('i').rstrip('o').rstrip('u')
for kwd in enumerate(no_contengan):
    no_contengan[kwd[0]] = kwd[1].rstrip('s').rstrip('a').rstrip('e').rstrip('i').rstrip('o').rstrip('u')
print('General use info:\n\n'
      'Input file must be named like this --> 20160512_3.csv\n'
      'First 8 numbers are year-month-date, whilst last number is the index of the\n'
      '\"keyword\" column, starting from zero.\n'
      'After the second number, you can add anything else to the file\'s name, as long\n'
      'as it end in .csv\n'
      'example: 20160603_2_eraser_negativas_borradas.csv\n\n'
      'When running the script, there must only be one csv in the same folder,\n'
      'the one to examine.\n'
      '                   vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n'
      '          -------->The file must be encoded in UTF-8<----------\n'
      '                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
      'There\'s no harm in adding extra columns to the file, but the mandatory ones are:\n'
      'Action, Campaign, Ad group, Keyword, Keyword state, Max. CPC, Final URL, Keyword ID,\n'
      'Ad group ID      :-->  The order doesn\'t matter\n\n'
      'There will be two output files: one to erase keywords containing \'bad\' terms,\n'
      'and another to add those who also include any of the \'good\' terms,\n'
      'but re-creating them in modified broad.\n\n')


def detect_delimiter(sample_line):
    if len(sample_line.split('\t')) > 1:
        return '\t'
    if len(sample_line.split(';')) > 1:
        return ';'
    if len(sample_line.split(',')) > 1:
        return ','
    input('Error: Delimiter wasn\'t detected as one of these values: \\t, ; or ,')
    raise SyntaxError('Delimiter wasn\'t detected as one of these values: \\t, ; or ,')

try:
    for file in os.listdir(os.path.dirname(__file__)):
        if file[-4:] != '.csv' or not(os.path.isfile(file)):
            continue
        try:
            input_handler = open(file, mode='r', encoding='utf-8')
        except UnicodeDecodeError:
            input('Error: Probably encoding is not utf-8')
            raise SyntaxError('Error: Probably encoding is not utf-8')
        break
    # It'll break if there is no csv file on the same directory as the python executable

    if re.match('[0-9]{8}_[0-9]+.*\.csv', input_handler.name) is None:
        input('file name ' + input_handler.name +
              ' doesn\'t comply with the structure <YYYYMMDD>_<COLUMN-ID>.csv\n\n'
              'Press enter to finish')
        raise NameError('file name ' + input_handler.name +
                        ' doesn\'t comply with the structure <YYYYMMDD>_<COLUMN-ID>.csv')
except:
    input('Error: no csv detected in the folder.')
    raise ValueError('Error: no csv detected in the folder.')
try:
    ColumnId = int(input_handler.name.split('_')[1].split('.')[0])
except ValueError:
    ColumnId = int(input_handler.name.split('_')[1])
output_handler = open(input_handler.name[:-4] + '_output.csv', mode='w', encoding='utf-8')
output_handler_add = open(input_handler.name[:-4] + '_output_add_keywords.csv', mode='w', encoding='utf-8')


def test_columns(first_line_bis):
    try:
        first_line_bis[first_line.index('Campaign')]
    except ValueError:
        input('No column named \"Campaign\" detected. This is mandatory. Aborting. Press enter to finish application.')
        raise ValueError('No column named \"Campaign\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Ad group')]
    except ValueError:
        input('No column named \"Ad group\" detected. This is mandatory. Aborting. Press enter to finish application.')
        raise ValueError('No column named \"Ad group\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Keyword state')]
    except ValueError:
        input('No column named \"Keyword state\" detected. This is mandatory. Aborting. '
              'Press enter to finish application.')
        raise ValueError('No column named \"Keyword state\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Keyword')]
    except ValueError:
        input('No column named \"Keyword\" detected. This is mandatory. Aborting. Press enter to finish application.')
        raise ValueError('No column named \"Keyword\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Max. CPC')]
    except ValueError:
        input('No column named \"Max. CPC\" detected. This is mandatory. Aborting. Press enter to finish application.')
        raise ValueError('No column named \"Max. CPC\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Final URL')]
    except ValueError:
        input('No column named \"Final URL\" detected. This is mandatory. Aborting. Press enter to finish application.')
        raise ValueError('No column named \"Final URL\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Keyword ID')]
    except ValueError:
        input('No column named \"Keyword ID\" detected. This is mandatory. Aborting. '
              'Press enter to finish application.')
        raise ValueError('No column named \"Keyword ID\" detected. This is mandatory. Aborting. '
                         'Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Ad group ID')]
    except ValueError:
        input('No column named \"Ad group ID\" detected. This is mandatory. Aborting.'
              ' Press enter to finish application.')
        raise ValueError('No column named \"Ad group ID\" detected. This is mandatory. Aborting.'
                         ' Press enter to finish application.')
    try:
        first_line_bis[first_line.index('Action')]
    except ValueError:
        if input('No column named \"Action\" detected. Are you sure you don\'t want this column to edit/delete '
                 'keywords?\n'
                 'Press enter to continue application or write no and press enter to abort.') == 'no':
            return 0
    return


def judgeline(fullline, kwds):
    global output_handler
    global output_handler_add
    global first_line
    global d

    contains = False
    dont_contains = False
    if kwds[0] == '':
        leading_blank = True
    else:
        leading_blank = False
    for kwd in kwds:
        try:
            contengan.index(kwd.lower().rstrip('s').rstrip('a').rstrip('e').rstrip('i').rstrip('o').rstrip('u'))
            contains = True
            break
        except ValueError:
            pass
    if contains is False and leading_blank is False:
        return None
    if contains is True:
        for kwd in kwds:
            try:
                no_contengan.index(kwd.lower().rstrip('s').rstrip('a').rstrip('e').rstrip('i').rstrip('o').rstrip('u'))
                dont_contains = True
                what = kwd
                break
            except ValueError:
                pass
    if action is True:
        output_handler.write('Delete' + d.join(fullline) + '\n')
    else:
        output_handler.write(d.join(fullline) + '\n')
    if dont_contains is False and leading_blank is False:
        return None
    if dont_contains is True:
        fullline[ColumnId] = fullline[ColumnId].replace(what, '+' + what)
    if leading_blank is True:
        fullline[ColumnId] = fullline[ColumnId].lstrip(' ')
    
    writeline = d.join([fullline[first_line.index('Campaign')], fullline[first_line.index('Ad group')],
                        fullline[ColumnId], fullline[first_line.index('Keyword state')],
                        fullline[first_line.index('Max. CPC')], fullline[first_line.index('Final URL')]])
    if action is True:
        output_handler_add.write('Add' + d + writeline + '\n')
    else:
        output_handler_add.write(writeline + '\n')




first = True
print('Starting to read file ' + input_handler.name)
i, u = 0, 0
try:
    for line in input_handler:
        i += 1
        if first:
            if line.find('Keyword report') != -1:
                print('Adwords download \"Keyword report\" line detected and skipped')
                continue
            first_line = line.rstrip('\n').rstrip('\r')
            d = detect_delimiter(first_line)
            first_line = first_line.split(d)
            if test_columns(first_line) == 0:
                print('Aborting...')
                import time
                time.sleep(2)
                print('..')
                time.sleep(2)
                print('.')
                time.sleep(1)
                raise ValueError('Commanded to abort')
            if line.split(d)[0] == 'Action':
                action = True
            else:
                action = False

            output_handler.write(line)
            if action is True:
                output_handler_add.write('Action' + d + 'Campaign' + d + 'Ad group' + d + 'Keyword' + d + 'Keyword state' +
                                         d + 'Max. CPC' + d + 'Final URL\n')
            else:
                output_handler_add.write('Campaign' + d + 'Ad group' + d + 'Keyword' + d + 'Keyword state' +
                                         d + 'Max. CPC' + d + 'Final URL\n')
            first = False
            continue
        if i % 100000 == 0:
            u += 1
            print('Processinbg line ' + str(u * 100000))
        line = line.rstrip('\n').rstrip('\r').split(d)
        if len(line[ColumnId].split(' ')) > 1:
            judgeline(line, line[ColumnId].split(' '))
        else:
            judgeline(line, line[ColumnId])
except UnicodeDecodeError:
    input('Error: Probably encoding is not utf-8')
    raise SyntaxError('Error: Probably encoding is not utf-8')

input('Script finished succesfully. Press enter to close window.')