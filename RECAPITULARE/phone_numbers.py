from os import read
import random as rnd


def generate_contact():
    # phone number
    pho_no = rnd.randint(1_111_111_111, 9_999_999_999)
    # name
    name = rnd.choice(['Liam','Olivia','Noah','Emma','Oliver','Charlotte','Elijah','Amelia','James','Ava','William','Sophia','Benjamin','Isabella','Lucas','Mia','Henry','Evelyn','Theodore','Harper1',])
    # locatie poza
    loc = 'file.jpg'
    # grup
    group = rnd.choice(['Family', 'Friends', 'Work', 'Football'])
    # favorit sau nu
    fav = rnd.choice([True, False])
    
    #<Numar_telefon> nume <valoare> locatie_poza <valoare> grup <valoare> favorit <valoare>
    return (pho_no, {'locatie_poza': loc, 'nume': name,  'grup': group, 'favorit': fav})



def generate_contacts(count):
    contacts = []

    # generate a contacts based on the count
    for _ in range(count):
        c = generate_contact()
        contacts.append(c)
    
    # print(contacts)

    with open("contacts.txt", 'w') as fp:
        #  contacts is a list of tuples in the format of (phone_number, details_dict)
        for phone_no, details in contacts:
            line = str(phone_no)
            for key in details:
                line += ' ' + ' '.join([key, str(details[key])])
            
            fp.write(line + '\n')

def read_contacts(filepath):
    contacts = {}
    with open(filepath, 'r') as fp:
        for line in fp:
            values = line.strip('\n').split(' ')

            # change it so that order of keys doesn't matter
            # phone_no = int(values[0])
            # name = values[subreddits]
            # pic = values[4]
            # group = values[6]
            # fav = True if values[8] == 'True' else False
            # ==============================
            for i in range(0,9):
                if int(len(values[i])) == 10:
                    phone_no = int(values[i])
                if values[i] == 'nume':
                    name = values[i+1]
                elif values[i] == 'locatie_poza':
                    pic = values[i+1]
                elif values[i] == 'grup':
                    group = values[i + 1]
                elif values[i] == 'favorit':
                    fav = True if values[i+1] == 'True' else False
                # phone_no = (lambda: int(values[i]) if int(len(values[i])) == 10 else 0)
            # Alex
            # ======================================
            phone_no = int(values[0])
            arg_names = values[1::2]
            arg_values = values[2::2]
            attrs = {key:val for key, val in zip(arg_names, arg_values)}

            name = attrs['nume']
            pic = attrs['locatie_poza']
            group = attrs['grup']
            fav = True if attrs['favorit'] == 'True' else False
            #======================================
            # if the contacts doesn't exist, add it
            if name not in contacts:
                contacts[name] = {
                    'number': [phone_no],
                    'locatie_poza': pic,
                    'grup': [group],
                    'favorit': fav
                }
            else:
                # add the details to the existing record
                contacts[name]['number'].append(phone_no)
                contacts[name]['grup'].append(group)
                contacts[name]['favorit'] = contacts[name]['favorit'] or fav

    return contacts



if __name__ == "__main__":

    CONTACTS_COUNT = 10
    # generate_contacts(CONTACTS_COUNT)


    CONTACTS_FILE = 'contacts.txt'
    contacts = read_contacts(CONTACTS_FILE)
    for name in contacts:
        print(name, contacts[name])