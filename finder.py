import random

heart = """
             .;;;, .;;;,                   .;;;, .;;;,
        .;;;,;;;;;,;;;;;,.;;;,       .;;;.,;;;;;,;;;;;,;;;.
       ;;;;oOOoOOoOOoOOoOOo;;;. .,. .;;;oOOoOOoOOoOOoOOo;;;;
   .,,.`oOOo'           `OoOOo,;;;;;,oOOoO'          `oOOo;',,.
  ;;;;oOOo'    ,;;;,       `OoOOo;oOOoO'       ,;;;,   `oOOo;;;;
  `;;OOoO'    ;;;'             `OOO'             `;;;   `OoOO;;'
 ,;;,OOoO     ;;                 "                 ;;    OoOO,;;,
 ;;;;OOoO     `;     ,;;.                          ;'    OoOO;;;;
  ``.;OOoO,    `;    ` ;;    .;;. ;; ;; .;;,      ;'   ,OoOO;,''
    ;;;;OOoO,          ;;    ;  ; `; ;' ;..'         ,OoOO;;;;
     ```.;OOoO,        ;,;;, `;;'  `;'  `;;'       ,OoOO;,'''
        ;;;;OOoO,      '    ',  ,                ,OoOO;;;;
         ```,;OOoO,.          ''              .,OoOO;,'''
             ;;;;OOoO,.                    .,OoOO;;;;
              ````,;OOoO,.              .,OoOO;, '''
                  ;;;;;OOoO,.        .,OoOO;;;;
                   `````,;OOoO,.  .,OoOO;,''''
                        ;;;;;OOoOOoOO;;;;;      
                         `````;;OO;;'''''
                              `;;;;'
"""
finder = """
    ___ _           _             
   / __|_)         | |            
 _| |__ _ ____   __| |_____  ____ 
(_   __) |  _ \ / _  | ___ |/ ___)
  | |  | | | | ( (_| | ____| |    
  |_|  |_|_| |_|\____|_____)_| 
 
 """
print(finder)
print("Witaj na portalu randkowym Finder.")


# Funkcja do walidacji wieku
def get_age():
    while True:
        try:
            age = int(input("Podaj swój wiek: "))
            if age < 18:
                print("Przykro nam, ale musisz mieć co najmniej 18 lat, aby uczestniczyć.")
                exit()  # Zakończ program, jeśli użytkownik ma mniej niż 18 lat
            return age
        except ValueError:
            print("Wprowadź prawidłowy wiek.")


# Funkcja do walidacji wzrostu
def get_height():
    while True:
        try:
            return float(input("Podaj swój wzrost w cm: "))
        except ValueError:
            print("Wprowadź prawidłowy wzrost w cm.")


# Funkcja do walidacji płci
def get_sex():
    while True:
        sex = input("Podaj swoją płeć (M/K): ").upper()
        if sex in ['M', 'K']:
            return sex
        else:
            print("Wprowadź prawidłową płeć (M lub K).")


# Pobieranie danych użytkownika
name = input("Podaj swoje imię: ").capitalize()
age = get_age()
sex = get_sex()
height = get_height()

# Lista przykładowych zainteresowań
interest_list = ["muzyka", "sport", "podróże", "sztuka", "gotowanie", "literatura", "technologia", "filmy", "teatr",
                 "nauka"]

# Wyświetlanie dostępnych zainteresowań
print("\nWybierz swoje zainteresowania z poniższej listy (wpisz numery oddzielone przecinkami):")
for i, interest in enumerate(interest_list, start=1):
    print(f"{i}. {interest}")

# Pobieranie zainteresowań użytkownika
chosen_interests_indexes = input("Twoje zainteresowania (numery): ").split(',')
chosen_interests = []

# Walidacja wybranych zainteresowań
for index in chosen_interests_indexes:
    try:
        index = int(index.strip()) - 1
        if 0 <= index < len(interest_list):
            chosen_interests.append(interest_list[index])
        else:
            print(f"Nieprawidłowy numer: {index + 1}. Ignorowanie.")
    except ValueError:
        print(f"Nieprawidłowe wejście: {index.strip()}. Ignorowanie.")

# Tworzenie profilu użytkownika
user_profile = {
    "name": name,
    "age": age,
    "sex": sex,
    "height": height,
    "interests": chosen_interests,
    "appearance": random.randint(1, 10)  # Ocena wyglądu użytkownika
}

# Lista imion męskich i damskich
male_names = ["Adam", "Adrian", "Aleksander", "Andrzej", "Artur", "Bartosz", "Błażej", "Damian", "Daniel", "Dawid", "Dominik", "Emil", "Filip", "Grzegorz", "Hubert", "Igor", "Jakub", "Jan", "Jarosław", "Jerzy", "Józef", "Karol", "Krzysztof", "Łukasz", "Maciej", "Marek", "Marcin", "Mateusz", "Mikołaj", "Mirosław", "Norbert", "Patryk", "Rafał", "Robert", "Ryszard", "Sebastian", "Sławomir", "Stanisław", "Stefan", "Szymon", "Tadeusz", "Waldemar", "Wiesław", "Wiktor", "Witold", "Wojciech", "Zbigniew", "Zdzisław", "Zenon", "Zygmunt"]
female_names = ["Alicja", "Amelia", "Aneta", "Barbara", "Beata", "Bogumiła", "Bożena", "Cecylia", "Dagmara", "Dorota", "Elżbieta", "Ewa", "Gabriela", "Grażyna", "Halina", "Helena", "Iga", "Irena", "Izabela", "Jadwiga", "Joanna", "Jolanta", "Julia", "Justyna", "Kamila", "Karolina", "Kinga", "Klaudia", "Krystyna", "Laura", "Lena", "Lidia", "Lucyna", "Magdalena", "Małgorzata", "Maria", "Marlena", "Martyna", "Milena", "Monika", "Natalia", "Nina", "Olga", "Patrycja", "Paulina", "Renata", "Roksana", "Sylwia", "Teresa", "Urszula"]

# Funkcja do generowania losowego profilu
def generate_random_profile(sex):
    if sex == "M":
        name = random.choice(male_names)
    else:
        name = random.choice(female_names)

    profile = {
        "name": name,
        "age": random.randint(18, 40),
        "sex": sex,
        "height": random.uniform(150, 190),
        "interests": random.sample(interest_list, 3),
        "appearance": random.randint(1, 10),  # Ocena wyglądu
        "distance": random.randint(1, 500)  # Odległość w km
    }
    return profile


# Funkcja do wyznaczania dopasowania
def is_match(user, partner):
    base_chance = 100 - abs(user['age'] - partner['age']) * 2  # Dopasowanie w zależności od wieku
    base_chance -= abs(user['appearance'] - partner['appearance']) * 2  # Dopasowanie w zależności od wyglądu
    base_chance = max(base_chance, 10)  # Minimalna szansa to 10%
    match_chance = random.randint(1, 100)
    return match_chance <= base_chance, base_chance


# Generowanie listy losowych potencjalnych partnerów
potential_matches = [generate_random_profile('M') if sex == 'K' else generate_random_profile('K') for _ in range(20)]

# Filtrowanie potencjalnych dopasowań w zależności od płci użytkownika
match_list = [match for match in potential_matches if match['sex'] == ('M' if sex == 'K' else 'K')]

print("\nPrzesuwaj profile w lewo (odrzuć) lub w prawo (zaakceptuj).")
swipes = 0
total_matches = 0
matched_profiles = []

# Główna pętla przeglądania profili
while match_list:
    match = match_list.pop(0)  # Pobierz pierwszy dostępny profil

    print("\nPotencjalny partner:")
    for key, value in match.items():
        if key == "appearance":
            print(f"{key.capitalize()}: {value}/10")
        elif key == "distance":
            print(f"{key.capitalize()}: {value} km")
        else:
            print(f"{key.capitalize()}: {value}")

    decision = input("Przesuń w prawo, aby zaakceptować, lub w lewo, aby odrzucić (P/L): ").upper()

    if decision == "P":
        matched, match_chance = is_match(user_profile, match)
        if matched:
            print(f"Znaleziono dopasowanie! Pasujesz do {match['name']}.")
            total_matches += 1
            matched_profiles.append(match)
        else:
            print("Niestety, nie ma dopasowania.")
    elif decision == "L":
        print("Odrzucono profil.")
    else:
        print("Nieprawidłowa opcja, wybierz P lub L.")

    swipes += 1
    print(f"Pozostałe profile do przeglądania: {len(match_list)}")

# Wyświetlanie całkowitej liczby dopasowań i listy profili do wyboru
print(f"\nKoniec przeglądania profili. Łączna liczba dopasowań: {total_matches}")

if matched_profiles:
    while True:
        # Wyświetlanie listy profili dopasowań
        print("\nDostępne dopasowania:")
        for i, profile in enumerate(matched_profiles, start=1):
            print(
                f"{i}. {profile['name']}, wiek: {profile['age']}, wzrost: {profile['height']:.2f} cm, wygląd: {profile['appearance']}/10, odległość: {profile['distance']} km, zainteresowania: {', '.join(profile['interests'])}")

        try:
            # Pobranie wyboru użytkownika
            choice = int(input("\nWybierz numer profilu, aby zobaczyć szczegóły lub wpisz 0, aby zakończyć: "))

            if 1 <= choice <= len(matched_profiles):
                chosen_profile = matched_profiles[choice - 1]
                print("\nWybrany profil:")
                for key, value in chosen_profile.items():
                    if key == "appearance":
                        print(f"{key.capitalize()}: {value}/10")
                    elif key == "distance":
                        print(f"{key.capitalize()}: {value} km")
                    else:
                        print(f"{key.capitalize()}: {value}")

                # Zapytanie użytkownika, czy chce zakończyć przeglądanie
                next_action = input(
                    "\nCzy chcesz uczynić ten profil swoją miłością? (T/N) lub wpisz P, aby wrócić do listy profili: ").upper()
                if next_action == "T":
                    print("\nTo jest miłość!")
                    print(heart)
                    break  # Przerwanie pętli, jeśli użytkownik wybrał profil
                elif next_action == "P":
                    print("\nPowrót do listy profili.\n")
                    continue  # Wróć do przeglądania listy dopasowań
                else:
                    print("Kontynuowanie przeglądania profili.\n")

            elif choice == 0:
                print("Zakończono wybór profilu.")
                break  # Wyjście z pętli, jeśli użytkownik nie chce kontynuować

            else:
                print("Nieprawidłowy wybór.")

        except ValueError:
            print("Wprowadzono nieprawidłowy numer.")
else:
    print("Nie znaleziono żadnych dopasowań.")
