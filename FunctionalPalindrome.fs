let isPalindrome (s:string) =
    let cleaned = s.Replace(" ", "").ToLower() //Cleans string by removing spaces and converting to lowercase
    let rec loop i =
        if i > cleaned.Length / 2 
        then true
        else cleaned.[i] = cleaned.[cleaned.Length-1-i] && loop (i + 1) //Recursively compares end to start
    loop 0
    //unit test
    isPalindrome "racecar" //true
    isPalindrome "abba" //true
    isPalindrome "abc" //false
