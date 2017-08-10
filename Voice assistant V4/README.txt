Each module/plugin MUST have "nothingCanDo", "execute", "procentCount"

procentCount should return 0 - if can't do anything with request, 1 - if can make everything.

nothingCanDo should return text with explanation why can't execute process

execute should return executed process and run what it must



Input modules must have "getText" attribute to receive and process with input from user.
Output modules should have "output" attribute to make output of made things.

You can use colors in your app:
        example:        from TextColors import bcolors
after this you will be able to use  Pink,Blue,Green,Red,ENDC,Bold,Underline,YellowFill,CrossOut,Black,Yellow,Purple,Gray, colors.
        example:        bcolors().Blue + some text you want to be colorized + bcolors().ENDC
