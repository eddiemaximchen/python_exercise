english='Monday','Tuesday','Wednesday'
french='Lundi','Mardi','Mercredi'
list(zip(english,french)) #一次把多個 tuple 轉成一個list
>>[('Monday','Lundi'),('Tuesday','Mardi'),('Wednesday','Mercredi')]

dict(zip(english,french))#一次把多個 tuple 轉成一個dict
>>{('Monday':'Lundi'),('Tuesday':'Mardi'),('Wednesday':'Mercredi')}
