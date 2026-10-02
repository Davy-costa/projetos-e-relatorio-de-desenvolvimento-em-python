# Projeto: Daily Expense Tracker (Gerenciador de Despesas Diárias)
#
# Programa de menu no terminal com loop infinito (while True) e break
# condicional. Permite:
#   1. Adicionar uma despesa
#   2. Listar todas as despesas
#   3. Calcular total e média das despesas
#   4. Limpar todas as despesas
#   5. Sair do programa
#   (qualquer outra opção -> mensagem de escolha inválida)

print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []
while True:
    escolha = input()

    if escolha == "1":
        nova = float(input())
        expenses.append(nova)
        print("Expense added successfully!")

    elif escolha == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    elif escolha == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            media = total / len(expenses)
            print(f"Total expense: {total}")
            print(f"Average expense: {media}")

    elif escolha == "4":
        expenses.clear()
        print("All expenses cleared.")

    elif escolha == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
