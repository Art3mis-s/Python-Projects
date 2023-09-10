import re

def main():
    # this parse is a variable which passes the user's input to the parse function.
    print(parse(input("HTML: ")))

#  This function "s" is responsible for extracting a YouTube URL from the input HTML.
def parse(s):
    # This line uses the re.search function to check if there is an <iframe> element in the input HTML
    if re.search(r"<iframe(.)*><\/iframe>", s):
        #  If an iframe element is found in the input HTML, this line uses another re.search to look for a YouTube URL within the HTML string. The regular expression is used to match the URL.
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        # This condition checks if a match for the YouTube URL was found in the input HTML.
        if url_pattern:
            #  If a match is found, this line attempts to capture the matched groups within the regular expression
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]

if __name__ == "__main__":
    main()


#src is like the internet link that tells your computer where to find a video or picture on a web page.