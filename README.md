# FUZZPOST

Swagger API 2.1 json of Postman fuzzing Variable setup tool


Enjoy some coffee while fuzzing!


---

## How To Postman Fuzzing

### Sample Running
```
PS C:\Users\hjshin\Desktop\archive\code> python FUZZPOST.py
fuzz method ? > (y/default:N)
fuzz url ? > (y/default:N)
fuzz header ? > (y/default:N)
fuzz body ? > (default:Y/n)
.json file path? >  postman_collection_1227_2_2.json
fuzzparam variable name ? (default:{{fuzzParam}})
ex) {{vairable}}
you can default value, just input "d"  > d

...

[*] saved postman_collection_1227_2_2_fuzz.json

```


### Whole process
```
1. POSTMAN Export Collection v2.1 
2. Run FUZZPOST.py 
3. Import json file at FUZZPOST
4. Get *original_name*_fuzz.json file at FUZZPOST
5. Run POSTMAN
6. *original_name*_fuzz.json file import to POSTMAN
7. load Data .csv file at Collection Runner Data
8. Run Collection
```

## Info


### .csv file format 
- First colum must to be placed fuzzing variable name ex) fuzzParam

```
fuzzParam
1
2
3
4
5
6
```

## Reference
- https://medium.com/@Magii/fuzzing-with-postman-599dce6317c7
- https://learning.postman.com/docs/sending-requests/variables/
