# Что такое переменная в языке Си?
- [ ] Функция, которая генерирует случайные значения
- [ ] Всё, что не является константой
- [x] Место для хранения данных, которое имеет имя и тип
- [ ] Память, которая выделяется для массивов

## :desc
Переменная в языке Си — это место в памяти для хранения данных, которое имеет имя и тип. Она позволяет программе сохранять и манипулировать значениями в процессе выполнения.

---


# Какой тип данных в языке Си используется для представления целых чисел?
- [ ] `float`
- [ ] `double`
- [x] `int`

## :desc
Тип данных `int` используется для представления целых чисел в языке Си. Его размер, как правило, 4 байта. С такой размерностью он может хранить целые числа в диапазоне от `-2147483648` до `2147483647`.

---

# Как объявить переменную целого типа в языке Си?
- [ ] `int;`
- [ ] `var a;`
- [x] `int a;`
- [ ] `int a()`

## :desc
Переменная целого типа в языке Си объявляется с использованием ключевого слова `int`, за которым следует имя переменной. Например, `int a;`.

Общий синтаксис объявления переменной: `<type> <name>;`

---

# Как объявить переменную с плавающей точкой в языке Си?
- [ ] `float x`
- [x] `float x;`
- [ ] `float(x);`
- [ ] `float x()`

---

# Что такое инициализация в языке Си?
- [ ] Процесс создания функции
- [ ] Процесс выделения памяти под переменную
- [x] Присвоение начального значения переменной при ее объявлении
- [ ] Присвоение значения переменной в любом месте программы

## :desc
Инициализация — это процесс присвоения начального значения переменной в момент ее объявления. Например, `int a = 10;` - это инициализация переменной `a` с начальным значением 10.

---

# Что происходит, если переменная не инициализирована?
- [ ] Она автоматически получает значение 0
- [ ] Она автоматически получает значение NULL
- [x] Она имеет неопределенное значение
- [ ] Она не может быть использована в программе

## :desc
Если переменная не инициализирована, она имеет неопределенное значение. Это может привести к непредсказуемому поведению программы.

---

# Чем инициализация отличается от объявления в языке Си?
- [ ] Инициализация выделяет память, а объявление нет
- [x] Инициализация присваивает начальное значение, а объявление только определяет тип и имя переменной
- [ ] Инициализация используется только для глобальных переменных, а объявление - для локальных
- [ ] Инициализация используется только для массивов, а объявление - для всех остальных переменных

## :desc
Объявление переменной определяет ее тип и имя, но не присваивает ей значение. Инициализация присваивает начальное значение переменной в момент ее объявления. Например, `int a;` - это объявление, а `int a = 10;` - это объявление с инициализацией.

---

# Можно ли инициализировать переменную после ее объявления?
- [ ] Да, это обязательно
- [ ] Нет, это невозможно
- [x] Да, но это не будет считаться инициализацией, а будет присваиванием
- [ ] Да, только если переменная глобальная

## :desc
Переменную можно инициализировать только в момент ее объявления. Присвоение значения переменной после объявления называется присваиванием. Например, `int a; a = 10;` - это объявление и последующее присваивание.

---

# Что произойдет, если попытаться использовать неинициализированную переменную?
- [ ] Компилятор выдаст ошибку
- [ ] Переменная автоматически получит значение 0
- [ ] Программа завершится с ошибкой
- [x] Поведение программы будет неопределенным

## :desc
Использование неинициализированной переменной приводит к неопределенному поведению программы, так как такая переменная имеет неопределенное значение.

---

# Как объявить константу целого типа в языке Си?
- [ ] `const int a;`
- [ ] `const a = 10;`
- [x] `const int a = 10;`
- [ ] `int a = const 10;`

## :desc
Константа целого типа в языке Си объявляется с использованием ключевого слова `const`, за которым следует тип переменной, ее имя и присваиваемое значение. Например, `const int a = 10;`. Константа создаётся только через *инициализацию*, поскольку это константа и ей нужно начальное значение :)

---

# Как объявить константу строкового типа в языке Си?
- [x] `const char *str = "Hello";`
- [ ] `char str[] = const "Hello";`

---

# Можно ли изменить значение константы после ее объявления?
- [ ] Да, с помощью функции
- [ ] Да, если использовать указатель
- [x] Нет, значение константы не может быть изменено после объявления
- [ ] Да, если использовать препроцессор

## :desc
После объявления значение константы не может быть изменено. Попытка изменения значения константы приведет к ошибке компиляции.

---

# Как использовать препроцессор для объявления константы в языке Си?
- [ ] `const int MAX = 100;`
- [ ] `const MAX 100;`
- [ ] `#define MAX const 100`
- [x] `#define MAX 100`

## :desc
Для объявления константы на этапе препроцессора используется директива `#define`, за которой следует имя константы и ее значение. Например, `#define MAX 100`.

---

# В чем разница между const и #define для объявления констант?
- [ ] `const` используется для числовых констант, а `#define` для строковых
- [ ] `const` может использоваться в функциях, а `#define` только глобально
- [x] `const` создает типобезопасные константы, а `#define` - текстовые замены
- [ ] `const` работает только с примитивными типами, а `#define` - с любыми

---

# Какое из следующих имен переменной допустимо в языке Си?
- [ ] `1variable`
- [x] `variable1`
- [ ] `var@name`
- [ ] `int`

## :desc
Имена переменных в языке Си не могут начинаться с цифры и не могут содержать специальные символы, такие как `@`. Ключевые слова, такие как `int`, также не могут быть использованы в качестве имен переменных. `variable1` - допустимое имя.

---

# Какое из следующих имен переменной допустимо в языке Си?
- [x] `_temp`
- [ ] `temp-variable`
- [ ] `temp variable`
- [ ] `temp.variable`

## :desc
Имена переменных в языке Си могут начинаться с символа подчеркивания `_`, но не могут содержать пробелы или точки. `-` также не допустим. `_temp` - допустимое имя.

---

# Какое из следующих имен переменной допустимо в языке Си?
- [ ] `float`
- [ ] `double`
- [x] `myVar`
- [ ] `char`

## :desc
Имена переменных в языке Си не могут быть ключевыми словами, такими как `float`, `double` или `char`. `myVar` - допустимое имя переменной.

---

# Какое из следующих имен переменной допустимо в языке Си?
- [x] `var_1`
- [ ] `123var`
- [ ] `var@123`
- [ ] `var-123`

## :desc
Имена переменных в языке Си могут содержать цифры, но не могут начинаться с цифры и не могут содержать специальные символы, такие как `@` или `-`. `var_1` - допустимое имя.

---

# Какие из следующих типов данных в языке Си используются для хранения целых чисел?
- [x] `char`, `short`, `int`, `long`
- [ ] `char`, `float`, `double`, `long`
- [ ] `short`, `int`, `long`
- [ ] `int`, `long`

## :desc
Типы данных `char`, `short`, `int`, `long` используется для хранения целых чисел в языке Си.

А их размер определяется по правилу: `char` <= `short` <= `int` <= `long`.

---

# Какой из следующих типов данных в языке Си используются для хранения чисел с плавающей точкой?
- [ ] `char`, `float`, `double`
- [x] `float`, `double`
- [ ] `short double`, `double`
- [ ] `void`, `float`

## :desc
Тип данных `float`, `double` используется для хранения чисел с плавающей точкой в языке Си.

А их размер определяется по правилу: `float` <= `double` <= `long double`.

---

# Какой из следующих типов данных в языке Си используется для указания на отсутствие значения или просто на ячейку в памяти (в случае с указателем)?
- [ ] `int`
- [ ] `float`
- [ ] `char`
- [x] `void`

## :desc
Тип данных `void` не имеет размера и используется для указания на отсутствие значения, например, в функциях, которые ничего не возвращают. Или на ячейку памяти в случае с указателем.

---

# Какой размер имеет тип данных `int` на большинстве современных платформ?
- [ ] 1 байт
- [ ] 2 байта
- [x] 4 байта
- [ ] 8 байт

## :desc
На большинстве современных платформ тип данных `int` имеет размер 4 байта.

---

# По какому правилу стандарт языка Си определяет размеры типов (в байтах)?
- [x] 1 <= `char` <= `short` <= `int` <= `long` <= `float` <= `double`
- [ ] `char` = 1, `int` = 4, `long` = 8, `float` = 4, `double` = 8 и тп.
- [ ] Никакому. Это отсаётся на усмотрение разработчиков компилятора или конкретной платформы.
- [ ] Всем базовые типы имеют размер 4 байта.

## :desc
Стандарт языка Си не определяет точных размеров типов, но требует, чтобы выполнялось правило, по которому тип `char` должен быть больше или равен 1 байту, тип `short` больше или равен `char` и тд.

Это правило можно выразить следующим: 1 <= `char` <= `short` <= `int` <= `long` <= `float` <= `double`.

Это связано с тем, что Си применяется на многих аппаратных платформах, где размеры памяти могут радикально различаться. Поэтому в этом аспекте стандарт даёт такую гибкость. Но, на подавляющем большинстве платформ, размеры типов являются привычными, где `char` = 1, `int` = 4, `double` = 8 и тд.

---


# Какой из следующих типов данных в языке Си используется для хранения беззнаковых целых чисел?
- [ ] `int`
- [ ] `float`
- [ ] `signed char`
- [x] `unsigned int`

---

# Какой из следующих типов данных в языке Си имеет наибольшую точность для чисел с плавающей точкой?
- [ ] `int`
- [ ] `float`
- [ ] `double`
- [x] `long double`

---

# Что такое "статическая переменная" в языке Си?
- [ ] Переменная, значение которой может изменяться только в определённые моменты выполнения программы
- [x] Переменная, которая сохраняет свое значение между вызовами функции
- [ ] Переменная, доступная только внутри определенной функции
- [ ] Переменная, которой значение можно присвоить только один раз

## :desc
Статическая переменная в языке Си - это переменная, которая сохраняет свое значение между вызовами функции. Она инициализируется только один раз, при первом вызове функции, и сохраняет свое значение на протяжении всего времени выполнения программы.

---

# Как объявить статическую переменную в функции в языке Си?
- [ ] `const int x;`
- [ ] `int static x;`
- [x] `static int x;`

## :desc
Статическая переменная в функции объявляется с использованием ключевого слова `static` перед типом данных переменной. Например, `static int x;`.

---

# Может ли статическая переменная быть объявлена в глобальной области видимости?
- [x] Да
- [ ] Нет
- [ ] Только если она константа
- [ ] Только если она внешняя

## :desc
Да, статическая переменная может быть объявлена в глобальной области видимости. В этом случае она будет доступна только внутри файла, в котором была объявлена.

---

# Что такое extern (внешняя) переменная в Си?
- [ ] Переменная, объявленная глобально
- [ ] Переменная, доступная только в пределах одного файла
- [x] Переменная, объявленная в одном файле и используемая в других
- [ ] Переменная, которая может быть изменена только извне

## :desc
`extern` переменная в языке Си — это переменная, которая объявляется в одном файле и может быть использована в других файлах. Она позволяет разделять общие глобальные переменные между разными файлами исходного кода, *что не рекомендуется делать, если на это нет веских оснований*.

---

# Как объявить внешнюю переменную в языке Си?
- [x] `extern int a;`
- [ ] `external int a;`
- [ ] `int extern a;`
- [ ] `ext int a;`

## :desc
Внешняя переменная в языке Си объявляется с использованием ключевого слова `extern` перед типом переменной. Например, `extern int a;`.

---

# Что такое явное преобразование типов в языке Си?
- [ ] Явное создание новой переменной от старого значения с другим типом
- [x] Явное и принудительное преобразование одного типа данных в другой
- [ ] Преобразование типов, выполняемое компилятором без вмешательства пользователя
- [ ] Явное преобразование типа, которое не изменяет значение переменной

## :desc
Явное преобразование типов (type casting) в языке Си - это принудительное преобразование одного типа данных в другой, выполняемое с помощью оператора приведения типов.

---

# Как выглядит синтаксис явного преобразования типов в языке Си?
- [x] `(new_type) expression`
- [ ] `[new_type] expression`
- [ ] `{new_type} expression`
- [ ] `<new_type> expression`

## :desc
Синтаксис явного преобразования типов в языке Си выглядит следующим образом: `(new_type) expression`, где `new_type` - это тип данных, к которому нужно привести `expression`. Например, `(int)3.14` - приведения значения 3.14 типа `double` к типу `int`.

---

# Какое значение будет у выражения `(int) 3.14` в языке Си?
- [ ] 3.14
- [ ] 4
- [x] 3
- [ ] 0

## :desc
Выражение `(int) 3.14` приведет число с плавающей точкой 3.14 к целому типу `int`, что даст значение 3.

---

# Что произойдет, если выполнить приведение типа `double` к `int`?
- [ ] Значение будет округлено до ближайшего целого
- [ ] Значение останется таким же
- [x] Дробная часть числа будет отброшена
- [ ] Будет выдано предупреждение компилятором

## :desc
При приведении типа `double` к `int` дробная часть числа будет отброшена, и останется только целая часть.

---

# Какое значение будет у выражения `(float) 5 / 2` в языке Си?
- [ ] 2
- [ ] 2.0
- [x] 2.5
- [ ] 2.0f

## :desc
Выражение `(float) 5 / 2` сначала приводит `5` к типу `float`, а затем деление `float` на `int` дает результат типа `float`, что равно 2.5.

---

# Какое значение будет у выражения `(int) (3.9 + 2.1)` в языке Си?
- [ ] 3
- [x] 6
- [ ] 5
- [ ] 7

## :desc
Сначала выполняется сложение `3.9 + 2.1`, что дает 6.0, а затем приведение к типу `int` отбросит дробную часть, и результат будет 6.

---

# Что произойдет при попытке привести строку к типу `int` в языке Си?
- [ ] Строка будет преобразована в числовое значение
- [ ] Программа завершится с ошибкой
- [x] Компилятор выдаст ошибку
- [ ] Строка будет преобразована в ноль

## :desc
Попытка привести строку к типу `int` приведет к ошибке компиляции, так как это недопустимая операция в языке Си.

---

# Какой результат будет у выражения `(int) 'A'` в языке Си?
- [x] 65
- [ ] 'A'
- [ ] 0
- [ ] -1

## :desc
Выражение `(int) 'A'` приведет символ `'A'` к его целочисленному представлению в кодировке ASCII, что равно 65.

---

# Какое значение будет у выражения `(char) 97` в языке Си?
- [ ] '9'
- [ ] '7'
- [x] 'a'
- [ ] 'A'

## :desc
Выражение `(char) 97` приведет целое число 97 к его символу в кодировке ASCII, что соответствует символу `'a'`.

---

# Что такое неявное преобразование типов в языке Си?
- [x] Автоматическое преобразование одного типа данных в другой, выполняемое компилятором
- [ ] Принудительное преобразование одного типа данных в другой, выполняемое программистом
- [ ] Создание переменной с типом `void`
- [ ] Преобразование типов, которое происходит при вызове функции

## :desc
Неявное преобразование типов (implicit type conversion) в языке Си - это автоматическое преобразование одного типа данных в другой, выполняемое компилятором, чтобы обеспечить совместимость типов в выражениях. Это возможно, поскольку Си хоть и является языком со статической типизацией, эта типизация является *слабой*, то есть более гибкой и допускающей неявные преобразования схожих типов.

---

# Какое правило применяется при неявном преобразовании типов в языке Си, если операнды разных типов?
- [x] Меньший тип всегда преобразуется к большему типу
- [ ] Больший тип всегда преобразуется к меньшему типу
- [ ] Операнды остаются своих типов, и компилятор выдает предупреждение

## :desc
В языке Си тип с меньшим размером (количеством допустимых значений) преобразуется к типу с большим размером. Это позволяет избежать потери данных.

---

# Какой тип данных будет результатом выражения `int_var + float_var`, где `int_var` - переменная типа `int`, а `float_var` - переменная типа `float`?
- [ ] `int`
- [x] `float`
- [ ] `double`
- [ ] `long`

## :desc
В выражении `int_var + float_var` компилятор неявно преобразует `int_var` к типу `float`, поскольку он является более "старшим" типом. Следовательно, результат будет типа `float`.

---

# Какое значение будет у выражения `5 + 2.5` в языке Си?
- [ ] 7
- [ ] 7.0
- [x] 7.5
- [ ] Ошибка компиляции

## :desc
В выражении `5 + 2.5` неявное преобразование типов приводит `5` к типу `double`, и результатом будет `7.5`. Литералы с плавующей точкой типа `2.5` всегда имеют тип `double`. Чтобы литерал имел тип `float`, нужно это явно указать с помощью постфикса `f`, например, `2.5f`.

---

# Какое значение будет у выражения `3 / 2` в языке Си?
- [x] 1
- [ ] 1.5
- [ ] 2
- [ ] Ошибка компиляции

## :desc
В выражении `3 / 2` оба операнда целочисленные, поэтому результатом будет целое число `1`, так как дробная часть будет отброшена.

---

# Какое значение будет у выражения `3 / 2.0` в языке Си?
- [ ] 1
- [ ] 1.0
- [x] 1.5
- [ ] Ошибка компиляции

## :desc
В выражении `3 / 2.0` компилятор неявно преобразует `3` к типу `double`, и результатом будет `1.5`.

---

# Что произойдет при присваивании `int_var = float_var`, где `int_var` - переменная типа `int`, а `float_var` - переменная типа `float`?
- [ ] Значение `float_var` будет округлено и присвоено `int_var`
- [ ] Значение `float_var` будет преобразовано в тип `int` и присвоено `int_var` с округлением
- [x] Значение `float_var` будет преобразовано в тип `int` с отбросом дробной части и присвоено `int_var`

## :desc
При присваивании `int_var = float_var` значение `float_var` будет неявно преобразовано к типу `int` с отбросом дробной части и присвоено `int_var`.

---

# Какое значение будет у выражения `char_var + 1`, где `char_var` - переменная типа `char` со значением 'A' (ASCII = 65)?
- [ ] 'A1'
- [ ] 'B'
- [x] 66
- [ ] Ошибка компиляции

## :desc
В выражении `char_var + 1` символ `'A'` (код ASCII 65) будет преобразован в целое число с типом `int`, поскольку операнд `1` имеет тип `int`. И результатом будет число 66 с типом `int`.

---

# Какой тип данных будет результатом выражения `unsigned_var + int_var`, где `unsigned_var` - переменная типа `unsigned int`, а `int_var` - переменная типа `int`?
- [ ] long
- [ ] int
- [x] unsigned int
- [ ] float

## :desc
В выражении `unsigned_var + int_var` компилятор неявно преобразует `int_var` к типу `unsigned int`, и результат будет типа `unsigned int`.

---

# Что произойдет при выполнении выражения `int_var * double_var`, где `int_var` - переменная типа `int`, а `double_var` - переменная типа `double`?
- [ ] Результатом будет значение типа `int`
- [ ] Результатом будет значение типа `float`
- [x] Результатом будет значение типа `double`
- [ ] Ошибка компиляции

## :desc
В выражении `int_var * double_var` компилятор неявно преобразует `int_var` к типу `double`, и результат будет типа `double`.

---

# Что произойдёт при преобразовании большего типа к меньшему?
- [ ] Компилятор выдаст ошибку
- [ ] Та часть, что не вмещается в меньший размер будет перемещена в специальный буферных раздел памяти для дальнейшего использования
- [x] Та часть, что не вмещается в меньший размер будет отброшена и произойдёт потеря значения этих битов
- [ ] Всё равно будет преобразование к большему типу

## :desc
В языке Си если происходит преобразование большего типа к меньшему, то "старший" тип просто усекается до размера меньшего с потерей значений в усечёных битах.

---