#1. 
a="softwarica"
print(a.upper())
#2.
a="@@PYTHON"
print(a.isupper())
#3.
a="@@PYTHON"
print("a".isupper())
#4.
a="capital"
print("A".isupper())
#5.
a="capital"
print("a")
#6.
a="capital"
print(a.capitalize())  #if i write "c" as given in the question then it gives back an error. But idk Why?
#7.
a="capital"
print(a.isalnum())
#8.
a="1Capital"
print(a.zfill(9))
#9.
a="+Capital"
print(a.zfill(9))
#10.
a="-Capital"
print(a.zfill(9))
#11.
a="$Capital"
print(a.zfill(9))
#12.
a="$Capital"
print(a.zfill(9))  #Yo ma if i add * after 9 like 9,"*" then we get an error, prolly cause zfill means zerofill and asterisk is not zero.
#13.
a="$Capital"
print(a.center(9,"*")) #Yo ma double asterisk rakhyao vane it gives error. So, i changed ** to *.
#14.
a="$Capital"
print(a.center(9,"*"))
#15.
a="+Capital"
print(a.center(9,"*"))
#16.
a="+Capital9"
print(a.count("9")) 
#17.
a="+Cap9ital9"
print(a.find("9"))
#18.
a="+Cap9ital9"
print(a.rfind("9"))
#19.
a="+Cap9ital9"
print(a.find("A"))
#20.
a="+Cap9ital9"
print(a.index("a")) #yesma when we add A then it gives error cause there is no A.
#21.
a="Cap9"
print(a.isdigit())
#22.
a="pythON9"
print(a.swapcase())
#23.
a="\t"
print(a.isspace())
#24.
a="\t"
print(a.isprintable())
#25.
a="123abc"
print(a.isalpha())
#26.
a="123abc"
print(a.rjust(11,"#"))
#27.
a="123abc"
print(a.ljust(11,"#"))
#28.
a="123abc"
print(a.ljust(6,"#"))
#29.
form="123abc"
print(form.ljust(6,"#")) #Yesma when we use for it gives error prolly cause its used for loop and can't be used as a variable name.
#30.
a="123abc"
print(a.replace('w',"1"))
#31
a="123abc"
b=a.count("c")
print(b)
#32.
a="123abc"
b=a.maketrans("123","abc") #confused!?
print(a.translate(b))
#33.
a="123abc"
b=a.maketrans("123","abc")
print(b)
#34.
a="123abc"
b=a.maketrans("A","a")
print(b)
#35.
a="123abc"
b=a.maketrans("abc","123")
print(b)
#36.
a="123abc"
b=a.startswith("123")
print(b)
#37.
a="123abc"
b=a.endswith("abc")
print(b)
#38.
a="123abc"
b=a.endswith("c")
print(b)
#39.
a="123abc"
print(a.replace('ab',"1"))