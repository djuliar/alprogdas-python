def menu():
    while True:
        print("\n=== User Management Menu ===")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            create_user(name, age)
        elif choice == "2":
            print("User List:")
            read_users()
        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, age)
        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Jalankan aplikasi
menu()

# Jangan lupa menutup koneksi
conn.close()