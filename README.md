### Порівняльний аналіз алгоритмів

Результати порівняння трьох алгоритмів сортування — вставками, злиттям та Timsort — за часом виконання на різних розмірах масивів:

| Розмір масиву | Сортування вставками | Сортування злиттям | Timsort |
| ------------- | -------------------- | ------------------ | ------- |
| 1000          | 0.04581              | 0.00592            | 0.00011 |
| 2000          | 0.15910              | 0.00719            | 0.00025 |
| 5000          | 1.29191              | 0.02233            | 0.00070 |
| 10000         | 4.80253              | 0.07043            | 0.00157 |

#### Аналіз результатів:

Сортування вставками показало значно гірші результати, особливо на великих масивах, що пояснюється його квадратичною часовою складністю
$ O(n^2) $

Це робить його непрактичним для великих даних.
Сортування злиттям виявилося значно швидшим, ніж сортування вставками, із часом виконання, що зростає більш стабільно. Це відповідає його теоретичній складності
$ 𝑂(𝑛\cdot log(𝑛)) $

Timsort є найшвидшим у всіх тестах. Завдяки поєднанню методів сортування злиттям і вставками, Timsort оптимізований для різноманітних реальних наборів даних, демонструючи високу ефективність навіть на великих масивах.

### Висновки:

Результати експерименту підтверджують, що Timsort є набагато ефективнішим порівняно з чистими алгоритмами сортування вставками та злиттям, особливо на великих масивах даних. Це обґрунтовує вибір Timsort як стандартного алгоритму сортування в Python, забезпечуючи високу продуктивність у загальних випадках використання.
