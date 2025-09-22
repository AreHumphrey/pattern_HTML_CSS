

### Уровень 1: Навигация и работа с файлами

1. **Создайте директорию `os_lab` в домашней папке и перейдите в неё.**
   ```powershell
   # PowerShell / cmd
   mkdir os_lab
   cd os_lab
   ```

2. **Создайте три пустых файла: `file1.txt`, `file2.log`, `note.md`.**
   ```powershell
   echo. > file1.txt
   echo. > file2.log
   echo. > note.md
   ```

3. **Выведите список всех файлов в текущей директории.**
   ```powershell
   # PowerShell
   Get-ChildItem
   # Или в cmd
   dir
   ```

4. **Создайте подпапку `docs` и переместите туда `note.md`.**
   ```powershell
   mkdir docs
   move note.md docs\
   ```

5. **Покажите полный путь к текущей директории.**
   ```powershell
   # PowerShell
   Get-Location
   # cmd
   cd
   ```

---

### Уровень 2: Работа с содержимым файлов

6. **Запишите строку "Hello OS!" в `file1.txt`.**
   ```powershell
   echo "Hello OS!" > file1.txt
   ```

7. **Добавьте строку "Lab started" в конец `file1.txt`.**
   ```powershell
   echo "Lab started" >> file1.txt
   ```

8. **Прочитайте и выведите содержимое `file1.txt`.**
   ```powershell
   # PowerShell
   Get-Content file1.txt
   # cmd
   type file1.txt
   ```

9. **Подсчитайте количество строк в `file1.txt`.**
   ```powershell
   # PowerShell
   (Get-Content file1.txt).Length
   # Альтернатива через wc (если установлен Git Bash)
   # Get-Content file1.txt | Measure-Object -Line
   ```

10. **Создайте файл `data.txt` и заполните его 10 строками чисел от 1 до 10 (по одной на строку).**
    ```powershell
    1..10 | ForEach-Object { Add-Content data.txt $_ }
    ```

---

### Уровень 3: Поиск и фильтрация

11. **Найдите все файлы с расширением `.txt` в текущей директории.**
    ```powershell
    # PowerShell
    Get-ChildItem -Filter *.txt
    # cmd
    dir *.txt
    ```

12. **Выведите только те строки из `data.txt`, которые содержат чётные числа.**
    ```powershell
    Select-String -Path data.txt -Pattern "2|4|6|8|10"
    ```
    *Или точнее:*
    ```powershell
    Get-Content data.txt | Where-Object { [int]$_ % 2 -eq 0 }
    ```

13. **Найдите строки в `data.txt`, содержащие число больше 5.**
    ```powershell
    Get-Content data.txt | Where-Object { [int]$_ -gt 5 }
    ```

14. **Скопируйте первые 3 строки из `data.txt` в новый файл `small.txt`.**
    ```powershell
    Get-Content data.txt | Select-Object -First 3 | Set-Content small.txt
    ```

15. **Отсортируйте содержимое `data.txt` в обратном порядке и сохраните в `sorted.txt`.**
    ```powershell
    Get-Content data.txt | Sort-Object { [int]$_ } -Descending | Set-Content sorted.txt
    ```

---

### Уровень 4: Обработка данных и комбинирование команд

16. **Подсчитайте общее количество строк во всех `.txt` файлах в текущей папке.**
    ```powershell
    (Get-Content *.txt | Measure-Object).Count
    ```

17. **Найдите самое длинное слово в `file1.txt`.**
    ```powershell
    $words = (Get-Content file1.txt) -split '\s+' | Where-Object { $_ }
    ($words | Sort-Object Length -Descending | Select-Object -First 1)
    ```

18. **Создайте архив (текстовый лог) с информацией: имя пользователя, дата, список файлов. Сохраните в `report.txt`.**
    ```powershell
    $user = $env:USERNAME
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"
    $files = (Get-ChildItem).Name -join ", "
    "$user | $date | Files: $files" | Out-File report.txt
    ```

19. **Удалите все пустые строки из `data.txt` и сохраните результат в `clean_data.txt`.**
    ```powershell
    Get-Content data.txt | Where-Object { $_.Trim() -ne "" } | Set-Content clean_data.txt
    ```

20. **Создайте файл `numbers.txt`, добавьте туда числа от 1 до 100, затем найдите и выведите сумму всех чисел.**
    ```powershell
    1..100 | Out-File numbers.txt
    $nums = Get-Content numbers.txt | ForEach-Object { [int]$_ }
    ($nums | Measure-Object -Sum).Sum
    ```

---



## Уровень 4.1: Работа с процессами и задачами



---

### 26. **Выведите список всех запущенных процессов.**

Подсказка:  
Используйте командлет `Get-Process`.  
Он показывает имя процесса, PID, потребление памяти и CPU.

Пример:
```powershell
Get-Process
```

---

### 27. **Найдите все процессы с именем "code" (если открыт VS Code) или "notepad".**

Подсказка:  
Передай имя процесса как параметр в `Get-Process`.  
Можно использовать фильтрацию по имени.

Команда:
```powershell
Get-Process notepad
```

---

### 28. **Отсортируйте процессы по объёму используемой памяти (WorkingSet) и покажите топ-5 самых «тяжёлых».**

Подсказка:  
Используй `Get-Process`, передай результат в `Sort-Object` по свойству `WS` (Working Set), отсортируй по убыванию (`-Descending`) и возьми первые 5 с помощью `Select-Object -First 5`.

Свойства процесса: `Name`, `Id`, `CPU`, `WS` (память в байтах).

---

### 29. **Проверьте, запущен ли процесс "chrome". Если да — выведите сообщение "Chrome работает", иначе — "Chrome не найден".**

Подсказка:  
- Используй `Get-Process` с именем `chrome`.
- Сохрани результат в переменную.
- Проверь, не пустая ли она (`$null` или нет).
- Используй `if`-условие.

Пустая переменная → `$null`.  
Пример проверки: `if ($proc -eq $null)`

---

### 30. **Остановите процесс по его PID (например, 1234), но только если он принадлежит приложению notepad.**

Подсказка:  
- Сначала найди процесс `notepad` через `Get-Process`.
- Убедись, что PID совпадает.
- Используй команду `Stop-Process -Id <PID>` или передай сам объект процесса.

⚠Будь осторожен: остановка чужих процессов может повлечь потерю данных.

---

### 31. **Создайте файл log.txt и запишите в него информацию о 3 процессах с самым высоким использованием CPU за последние 5 секунд.**

Подсказка:  
- Запроси процессы дважды с задержкой (через `Start-Sleep 5`).
- Или просто используй `Get-Process`, отсортируй по `CPU -Descending`.
- Возьми первые 3, преобразуй в строки (имя + CPU), и запиши в файл через `Out-File`.

Свойство: `CPU` — суммарное время CPU в секундах.

---

### 32. **Найдите все процессы, которые используют более 100 МБ оперативной памяти.**

Подсказка:  
- Получи все процессы.
- Отфильтруй через `Where-Object`: сравни `WS` (в байтах) с `100MB`.
- В PowerShell: `100MB` — это встроенная константа.

Пример условия:
```powershell
Where-Object { $_.WS -gt 100MB }
```

---

### 33. **Сохраните текущий список процессов в JSON-файл processes.json.**

 Подсказка:  
- Получи процессы через `Get-Process`.
- Выбери нужные поля (Name, Id, CPU, WS).
- Передай в `ConvertTo-Json`, затем в `Set-Content`.


```powershell
| Select-Object Name, Id, CPU, WS | ConvertTo-Json | Set-Content processes.json
```

---

### 34. **Запустите блокнот (notepad), подождите 3 секунды, затем найдите его процесс и завершите.**

Подсказка:  
- Запусти: `notepad` (или `Start-Process notepad`)
- Жди: `Start-Sleep 3`
- Найди процесс: `Get-Process notepad`
- Останови: `Stop-Process`

---

### 35. **Выведите общее количество запущенных процессов в данный момент.**

- Получи процессы.
- Передай в `Measure-Object`.
- Или используй `.Count` у массива.

Пример:
```powershell
(Get-Process).Count
```

---

### Полезные свойства процессов

| Свойство     | Описание                          |
|-------------|-----------------------------------|
| `Name`      | Имя исполняемого файла            |
| `Id` (PID)  | Идентификатор процесса             |
| `CPU`       | Время использования CPU (сек)     |
| `WS`        | Объём рабочей памяти (в байтах)    |
| `VM`        | Виртуальная память                 |
| `Path`      | Путь к исполняемому файлу          |



### Уровень 5: Продвинутые задачи 

21. **Создайте 5 директорий: `dir1`, `dir2`, ..., `dir5`, каждую с файлом `info.txt` внутри, содержащим имя директории.**
    ```powershell
    1..5 | ForEach-Object {
        $dir = "dir$_"
        mkdir $dir
        "Directory: $dir" | Out-File "$dir\info.txt"
    }
    ```

22. **Найдите все файлы, созданные сегодня, и выведите их имена и размер.**
    ```powershell
    Get-ChildItem | Where-Object { $_.CreationTime.Date -eq (Get-Date).Date } | 
        Select-Object Name, Length
    ```

---

# Блок 2



### Переменные
В PowerShell переменные начинаются с `$`.

```powershell
$age = 25
$name = "Alice"
$isStudent = $true
```

---

### Условие (if-else)
```powershell
if ($age -gt 18) {
    Write-Host "Совершеннолетний"
} else {
    Write-Host "Не достиг совершеннолетия"
}
```

Операторы сравнения:
- `-eq` — равно
- `-ne` — не равно
- `-lt` — меньше
- `-le` — меньше или равно
- `-gt` — больше
- `-ge` — больше или равно

---

### Цикл for
```powershell
for ($i = 1; $i -le 5; $i++) {
    Write-Host "Итерация $i"
}
```

---

### Цикл foreach
```powershell
$colors = "red", "green", "blue"
foreach ($color in $colors) {
    Write-Host "Цвет: $color"
}
```

---

### Цикл while
```powershell
$count = 0
while ($count -lt 3) {
    Write-Host "Счётчик: $count"
    $count++
}
```

---

## Задания 



---

1. **Создайте переменную `$temperature` со значением 37. Напишите условие: если температура > 36.6, выведите "Жарко", иначе — "Норма".**

   Пример начала:
   ```powershell
   $temperature = 37
   if ($temperature -gt 36.6) { ... }
   ```

---

2. **Создайте переменную `$score` (оценка от 0 до 100). Если `$score` >= 80, выведите "Отлично", иначе — "Нужно учиться".**

---

3. **Создайте переменную `$name` со своим именем. Если длина имени больше 5 символов, выведите "Длинное имя", иначе — "Короткое имя".**

   Подсказка: используйте `.Length`.

---

4. **С помощью цикла `for` выведите числа от 1 до 10.**

---

5. **Создайте массив `$fruits = "яблоко", "банан", "апельсин"`. С помощью `foreach` выведите каждый фрукт с приставкой "Любимый фрукт: [фрукт]".**

---

6. **Создайте переменную `$number = 1`. С помощью `while` увеличивайте её на 1, пока значение не станет больше 5. На каждой итерации выводите текущее число.**

---

7. **Создайте переменную `$isRaining = $true`. Если идёт дождь (`$isRaining`), выведите "Возьми зонт", иначе — "Можно идти без зонта".**

---

8. **Создайте переменную `$age = 17`. Проверьте: если возраст >= 16, выведите "Можно водить машину", иначе — "Пока рано".**

---


11. **Создайте переменную `$time = 14`. Если время < 12 — "Доброе утро", если от 12 до 18 — "Добрый день", иначе — "Добрый вечер". Используйте `if-elseif-else`.**

---

12. **С помощью цикла `for` выведите чётные числа от 2 до 10.**

---

13. **Создайте переменную `$password = "secret123"`. Если длина пароля меньше 8 символов, выведите "Слабый пароль", иначе — "Надёжный пароль".**
```powershell
$password.Length
```
---


