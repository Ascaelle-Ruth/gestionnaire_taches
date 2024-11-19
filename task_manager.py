tasks = []

def add_task():
    task = input("Entrez une nouvelle tâche : ")
    tasks.append(task)
    print("Tâche ajoutée !")

def show_tasks():
    if not tasks:
        print("La liste des tâches est vide.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def mark_task_as_done():
    show_tasks()
    try:
        task_number = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] += " (terminée)"
            print("Tâche mise à jour !")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Nouvelle fonctionnalité : Trier les tâches par ordre alphabétique
def sort_tasks():
    if not tasks:
        print("La liste des tâches est vide, rien à trier.")
    else:
        tasks.sort()
        print("Les tâches ont été triées par ordre alphabétique.")
        show_tasks()

# Menu principal
while True:
    print("\nChoisissez une action :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Trier les tâches par ordre alphabétique")
    print("5. Quitter")


    choice = input("> ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_as_done()
    elif choice == '4':
        sort_tasks()
    elif choice == '5':
        print("Au revoir !")
    else:
        print("Choix invalide.")
