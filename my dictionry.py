# dict1={"one":1,"two":2,"three":3}
# dict2={"four":4,"five":5,"six":6}
# #merge two dictionaries in one

# dict1.update(dict2)
# print(dict1)   


dict1={
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }

        }
    }
}

marks=dict1.get("class").get("student").get("marks").get("web")
print(marks)
