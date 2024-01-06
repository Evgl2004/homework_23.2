## Задание 1
Создайте группу для роли модератора и опишите необходимые доступы:

-  может отменять публикацию продукта,
-  может менять описание любого продукта,
-  может менять категорию любого продукта.

Недостающее поле признака публикации необходимо добавить таким образом, чтобы можно было определять статус продукта. 
Можно использовать BooleanField со значением False по умолчанию или CharField с указанием вариантов значений (choises).
При этом по умолчанию должен быть вариант, который не предполагает публикацию продукта.

## Задание 2
Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.

## * Дополнительное задание
Выделите отдельную роль для пользователя контент-менеджера, который может управлять публикациями в блоге.
Также не забудьте реализовать проверки на то, что обычный пользователь или модератор из другого отдела не сможет ничего изменить в разделе блога.