def get_quils_data():
    import csv
    import requests
    import io
    
    response = requests.get('https://docs.google.com/spreadsheets/d/1ndHX9YF8Q8NgwQ_vhwcuoJpU9lrZ6MXm2pbNc6jpPAU/export?format=csv&gid=1553811417')
    response.raise_for_status()
    quils_data_csv_string = response.text.replace('\r','')
    
    csv_file_object = io.StringIO(quils_data_csv_string)
    quils_data = list(csv.reader(csv_file_object))
    
    name_correction = {
        'LoveyDovey': 'Loveydovey',
        'PrickleFluff': 'Pricklefluff',
    }
    
    name_idx = quils_data[0].index('Dragon')
    for idx, row in enumerate(quils_data):
        name = row[name_idx]
        if name in name_correction.keys(): quils_data[idx][name_idx] = name_correction[name]
        
    return quils_data

def get_quils_earning_data(quils_data):
    name_idx = quils_data[0].index('Dragon')
    elder_idx = quils_data[0].index('Is Elder')
    earn_gold_idx = quils_data[0].index('Earn Gold')
    earn_etherium_idx = quils_data[0].index('Earn Etherium')
    earn_gems_idx = quils_data[0].index('Earn Gems')
    
    quils_earning_data = {}
    
    for row in quils_data[1:]:
        earning_dict = {}
        for title, earn_idx in [('Earn Gold', earn_gold_idx), ('Earn Etherium', earn_etherium_idx), ('Earn Gems', earn_gems_idx)]:
            if row[earn_idx] != '':
                earning_dict[title] = int(row[earn_idx])
        if earning_dict != {}:
            earning_dict['Is Elder'] = row[elder_idx] == '1'
            quils_earning_data[row[name_idx]] = earning_dict

    return quils_earning_data