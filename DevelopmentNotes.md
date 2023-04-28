# Development Notes

**Remember to activate the testing environment!**

Learn about Python environments!

Once you're done, you may **deactivate the environment**.

## TODO

  if (ongoingStop & ({message.author} == ongoingStopUser)):
  UnboundLocalError: local variable 'ongoingStop' referenced before assignment

1. Test functions, param and globals.

- def myfunction()
- bool = myfunction()
- bool = myfunction() # uses global variable.

1. $stop command to stop [stop the instance].
  <https://aws.plainenglish.io/the-fear-of-boto3-how-to-stop-ec2-instances-using-python-f0339a8ec986>

Command is:

  ec2.Instance('{INSTANCE-ID}').stop()

Therefore, we need to get the instance name in the discord chat to be able to stop the bot. Log message uses it(?)

1. Create a non-admin user in AWS.
    1. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html> to change default user and password.

1. CONFIG

1. $help = list of bot commands

1. README
  Add functionality description.
1. Use database to store lists of words.
1. $question - record somebody asked something.
    1. Set reminder (May anybody answer {question.user}, please?)
    1. Store $question in database.
    1. Set reminder period in .env
    1. $answer
    1. Match $answer with $question -> move to #q&a channel
    1. Clean $question from database

1. $meeting schedules a meeting: store it in db, publish it in #agenda channel, set reminder 30 min. ahead.
1. $translate:LL str translates the string to language LL by calling (deepl|google) API.

- [Getting Started with the DeepL Language Translation API in Python](https://thenewstack.io/getting-started-with-the-deepl-language-translation-api-in-python/)
-[deepl-python in GitHub](https://github.com/DeepLcom/deepl-python)

1. Increase Security against MitM attacks: [(Optional) Get the instance fingerprint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)
1. Store Servers where the bot is used. Keep track!
1. Alternative database

## Deploy in AWS

Following this procedure:<https://victormerino.medium.com/running-a-python-script-24-7-in-cloud-for-free-amazon-web-services-ec2-76af166ae4fb>

The step "We can access our instance using SSH using this command" does not work.

I use this to connect to the instance using ssh:<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html>

See file publicDNS.txt for instance setting details.

## Solving Unexpected Crashes

- [A Minimal Bot](https://discordpy.readthedocs.io/en/stable/quickstart.html) includes the right call to `discord.Client`.
- How to pass the token to the client: <https://stackoverflow.com/questions/73440592/typeerror-expected-token-to-be-a-str-received-class-nonetype-instead>
- [How to use dotenv package to load environment variables in Python](https://www.python-engineer.com/posts/dotenv-python/)
- `Presence Intent` and `Message Content Intent` privileged intents must be authorised in <https://discord.com/developers/applications> settings
- The `requests` module is not built-in as explained in [ImportError: No module named requests](https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests). It must be imported by using the following command:

    sudo apt-get install python3-requests

- The discord module is not found.

  sudo apt install pythonpy
  pip install -U discord.py

- No module named 'dotenv'

  pip install python-dotenv

## Resources

- [AWS CLI](https://pypi.org/project/awscli/)  provides a unified command line interface to Amazon Web Services.
- [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
- [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
- [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

### To Use

These are resources to add further features to the original project:

- Stop an AWS instance.

  - <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html>
  - <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html>

- Get info about the instance: <https://www.ktexperts.com/how-to-get-instance-details-by-using-boto3/>

- To use databases with Python.
  - [Do You Know Python Has A Built-In Database?](https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd)
  - [Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
  - [Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp)

### On the Project

- [The Tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- [The Video](https://www.youtube.com/watch?v=SPTfmiYiuok)
- The [list of projects](https://www.freecodecamp.org/news/python-projects-for-beginners/#code-a-discord-bot-with-python-host-for-free-in-the-cloud) where I found the tutorial.
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Used References

- Use AWS instead of repl.it.
  - [Running a Python script 24/7 in Cloud FOR FREE (Amazon Web Services EC2)](https://victormerino.medium.com/running-a-python-script-24-7-in-cloud-for-free-amazon-web-services-ec2-76af166ae4fb)
  - [How To Run Your Python Scripts in Amazon EC2 Instances (Demo)](https://towardsdatascience.com/how-to-run-your-python-scripts-in-amazon-ec2-instances-demo-8e56e76a6d24)

### On Python Development

- [Get started using Python for web development on Windows](https://learn.microsoft.com/en-us/windows/python/web-frameworks)
-

### Alternative Projects

- [DevOps With Python (Learning Path) – Real Python](https://realpython.com/learning-paths/python-devops/) ~ 7h with a very roughly approximation.
- [4 Practical Projects to Learn AWS](https://www.beabetterdev.com/2022/07/08/4-practical-projects-to-learn-aws/)
- [10 Best AWS Projects to Better your Learning](https://hackr.io/blog/best-aws-projects)
- [Free Cloud Computing Services - AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free+Tier+Types=*all&awsf.Free+Tier+Categories=*all&awsf.Free+Tier+Types=tier%23always-free&awsf.Free+Tier+Categories=*all)
- [Hands-On Tutorials for Amazon Web Services (AWS)](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=*all&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all)
