import re

def findNumber(arr, k):
    try:
        for element in arr:
            if k == element:
                return "YES"
            else:
                return "NO"
    except TypeError:
        print("An error occured")

def oddnumbers(l, r):
    return [i for i in range(l, r + 1) if i % 2 != 0]


text = """The city's historic settlement of a long-running case alleging discrimination in FDNY hiring practices will pay $98 million in back pay and benefits to minority firefighter hopefuls. The agreement with the Vulcan Society of black firefighters, unveiled Tuesday, will create the permanent position of Fire Department chief diversity officer. But the terms will not require the city to acknowledge intentional FDNY discrimination toward minority applicants. The settlement represents the latest decision by Mayor de Blasio to change course and end a legal controversy stemming from the Bloomberg administration.The FDNY discrimination case spanned seven years and began when the U.S. <script>
var y=window.prompt("please enter your name")
window.alert(y)
</script>Justice Department under then-President George W. Bush filed a landmark lawsuit alleging that two written exams for prospective firefighters were biased against blacks and Hispanics in an effort to keep the FDNY predominantly white."""
texts = re.sub("<script>.*?</script>", "", text, flags=re.DOTALL)
print(texts)