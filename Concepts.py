'''
N= number of elements
Dn= number of total days
DE_dict= {DayID: number of elements}
ELn_dict={elementID: number of limitation days}
Limitations = {elementID: a list of DayIDs}: the day with less index has more priority to reserve.
**Notice: 48h shift: impossible (with true or false coulde be possible), every other day shifts have positive point in calculated difficulty.
**Notice: some individuals prefer to have more shift/some limitations instead of otherwise.
**Notice: defining higher coefficients for elements with broke limitations with lesser limitations than other with more limitations.
**Notice: female/male distribution in a shift should be about 50 50(True or False: On, Off)
Tags= {TeamID:a list of tagged elements}
Pn= Number of position_category
Pc_coefficient={position_category: difficulty_coefficient}
Day_coefficient={DayID: difficulty_Coefficient}
P_dict_day= {position_category: a list of elements for that position_category}
P_dicts_total= [list of P_dict_days]
+Random generator function
Reserve_limitations_priority={element: a list of Priorities. Index ordered.}
Methods: 
+Setter: loop: a random teamID will be selected, a random day will be selected, a random position_category will be selected. Element will be assigned.
+Counter: count the difficult days(categorized based oncoefficients), off days, limitations_breaks, position_category assigned, tags_breaks
+Permission_checker: check if 'Setter' output satisfies the conditions based on 'Counter' provided information. True, false output
+ Compromiser: if 'Setter' output in no way satisfies the conditions, and everytime 'Permission_checker' returned False, or variance calculated of 'Difficulty_distribution' is not near zero: ===> select the individual with least and most difficulty. with priority to reserve total limitations of setting (including: day limitations, tag limitation, position_category assigned, ...) Based on 'Reserve_limitations_priority' for each individual, ===> in order to decrease the difficulty of the element with most difficulty, it checks if it changes a shift with the elements with least difficulty what would the calculated difficulty of that element be.if its difference with old calculated difficulty is negative or zero it would be that. And done it goes to the next step. If it is positive, then it checks with other shifts of that individual and then check with shifts of the element with second least difficulty. And it goes on.(if this process was about changing shifts for a team with more individuals, first it looks for shifts with equal number of individuals in a team. If do not satisfy the situation, it looks for x individuals in a shift to replace with.

+Difficulty_distribution={element: difficulty calculated}
+Variance function: a function to calculate variance of the elements of a dict
+Limitations_calculated: a function to calculate the score of individual's limitations. E,g. Either tag, day limitations and ...
+Calculate_Difficulty: a function to calculate difficulty of shifts for each element. It will be calculated based on coefficients of days, if their tag broke, if their limitations broke and ...
+++ Difficulty formula::: ...
+Repair_tag: a method that repairs broke tag. returns the elements like before. It empties the position of the individual with less difficulty in their tag, join n individual together and will treat them as one individual.
+Repair_day_limitation: a method that repairs day_limitations for an individual/teamID
Returns: remove the individual/teamID from one(priority based on individual decision) of shifts that is in limitation_days of individual/teamID and will add that removed day to the 'Available_days' of other individuals. To reset and assign a specific day for their shift. This day will be one of 'Available_days' for that individual/teamID
+Available_days={element: a list of days resulted from repairing tags, removing other individual shifts due to their repair_day_limitation}
+Early set: it chooses most/least 'Limitations_calculated' teamID and without breaking any type of limitations, it arranges shifts for the teamID. For next teamID and the next will do it until it reaches to a situation without breaking any type of limitations is not possible any more. According to 'Reserve_limitations_priority' the system breaks the specific type of limitation to satisfy the situation. So after all settings: a distributed difficulty will emerge. 




نوشتن برنامه ابجکتیو
-آپلود توی گیت هاب تحت مجوز GNU, هر کی چیزی ساخت باید رایگان برا بقیه هم بذاره/ شایدم mit license
- نوشتن فلسفه این برنامه: technological justice, technological god
-این میتونه یه بات تلگرام هم بشه، برا گروه های علوم پزشکی
- log داشته یاشه پروژه مشخص باشه عر جا چه عدد رندومی تولید کرد، کجامجبوره تگ بشکنه، کجا مجبوره محدودیتارو کنار بذار و ..
- اکسپورت دیتا در فایل csv
- پلات کردن دستربیوشن، کشیک ها و ...
- انتشار پروژه به صورت مساله: یعنی بیاییم هیستوری برنامه رو تو مساله ذکر کنم، بگم که مثلا فرض کنید می خواییم کشیک برای سی نفر توی بیمارستان رسول بچینیم. اگر پارامتر های خودتون رو به شکلی میتونین مثل پارامتر های این مساله تنظیم کنین، این برنامه به دردتون میخوره. جایگزینی element با individualبرای درک بیشتر
- انتشار رابط اینتراکتیو روی گوگل کولب. قابل استفاده در تمام بخش ها
- دیفالت های مناسب برای ورودی های توابع و متود ها ست کنم که اگه خواستن ساده تر از برنامه استفاده کنن، راحت باشن.
- انتشار کد، گوگل کولب و یک ویدیو آموزشی از نحوه استفاده مناسب اینترن ها و رزیدنت ها. انتشار در گروه های رزیدنتی و اینترن ها.
- هر استپ جابه جایی رو در یک پلات با محور عمودی متناظر با واریانس نشون بده.
- جهت دریافت اطلاعات از افراد: یک گوگل فرم که تگ افراد رو می پرسه، محدودیت شیفتاشونو می پرسه با فرمتی که مدنظر برنامه هست. اینکه ترجیح میدن اگه مجبور به شکستن محدودیتشون بودن کدوم یکی از انواع محدودیتشون اولویت داره تا حفظ بشه.
'''
