# Development Notes

**Remember to activate the testing environment!**

Learn about Python environments!

Once you're done, you may **deactivate the environment**.

## TODO

1. Dockerize the project.
1. $question - record somebody asked something.
    1. Set reminder (May anybody answer {question.user}, please?)
    1. Store $question in database.
    1. Set reminder period in .env
    1. $answer
    1. Match $answer with $question -> move to #q&a channel
    1. Clean $question from database

1. Make encouragements case-insensitive.

1. Randomize greetings.

1. $meeting schedules a meeting: store it in db, publish it in #agenda channel, set reminder 30 min. ahead.

- <https://stackoverflow.com/questions/8600161/executing-periodic-actions>
- <https://superfastpython.com/thread-periodic-background/>
- <https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679>

1. Clarify Amazon login: .pem file, fingerprint, etc.

  The authenticity of host 'ec2-52-28-48-82.eu-central-1.compute.amazonaws.com (52.28.48.82)' can't be established.
  ED25519 key fingerprint is SHA256:DmKx0TxK+s3qS8WcOcUAtZLhJi0P4Id41lRHGMHEWHU.
  This host key is known by the following other names/addresses:
      ~/.ssh/known_hosts:7: [hashed name]
      ~/.ssh/known_hosts:10: [hashed name]
  Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

1. Include some sort of dictionary to demonstrate the data structure.
  Article by Mustafa: <https://www.kaggle.com/code/mustafagerme/06-dictionaries-in-python>

1. Stop the bot. $stop command.
  It must close the database connection to make sure all data is recorded on disk.

1. DO NOT IMPLEMENT $stop command to stop [stop the instance].
  <https://aws.plainenglish.io/the-fear-of-boto3-how-to-stop-ec2-instances-using-python-f0339a8ec986>

Command is:

  ec2.Instance('{INSTANCE-ID}').stop()

Therefore, we need to get the instance name in the discord chat to be able to stop the bot. Log message uses it(?)

1. Create a non-admin user in AWS.
    1. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html> to change default user and password.

1. CONFIG

1. README
  Add functionality description.

- [Getting Started with the DeepL Language Translation API in Python](https://thenewstack.io/getting-started-with-the-deepl-language-translation-api-in-python/)
-[deepl-python in GitHub](https://github.com/DeepLcom/deepl-python)

1. Increase Security against MitM attacks: [(Optional) Get the instance fingerprint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)
1. Store Servers where the bot is used. Keep track!
1. Alternative database

## Discord API

<https://discordpy.readthedocs.io/en/stable/api.html#discord.Member>
<https://discordpy.readthedocs.io/en/stable/search.html?q=channel>
<https://discordpy.readthedocs.io/en/stable/api.html?highlight=channel#discord.Client.get_channel>
<https://discordpy.readthedocs.io/en/stable/api.html?highlight=channel#discord.Client.get_all_channels>

## sqlite3 database

CLI to SQLite3
<https://www.sqlite.org/cli.html>

<https://docs.python.org/3/library/sqlite3.html>
<https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection>
<https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-context-manager>
<https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders>

<https://www.sqlite.org/lang_returning.html>
<https://dzone.com/articles/use-returning-clause-to-avoid-unnecessary-sql-stat>

<https://manpages.ubuntu.com/manpages/jammy/en/man1/sqlite3.1.html>

Use `.schema tablename` to see the description of a table.
<https://www.sqlitetutorial.net/sqlite-describe-table/>

Use `.help` and `.quit` for obvious commands.
Use `select * from tablename;` and other SQL commands, when needed.

Dates are stored as text, and may be retrieved in different ways.
<https://www.sqlite.org/lang_datefunc.html>

Use sqlite3 from Python: <https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd>

## The Python Requirements File and How to Create it

Read <https://learnpython.com/blog/python-requirements-file/> but go first to the sections **How to Create Python Requirements File After Development** and **Best Practices for Using a Python Requirements File**.

Create the `requirements.txt` file from the `import`s of the `.py` files:

    ~/.local/bin/pipreqs --force .

    # check for missing dependencies in your python installation (not only in your project)
    python3 -m pip check

    # make sure all python modules are updated.
    # this is not an optimal solution. see https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
    pip list --outdated | awk 'NR > 2 { print $1 }' | xargs -n1 pip install -U

It is also possible to upgrade everything with `pip install -U -r requirements.txt`.

Drop the first lines of a text file: <https://unix.stackexchange.com/questions/37790/how-do-i-delete-the-first-n-lines-of-an-ascii-file-using-shell-commands>

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
  - <https://www.sqlitetutorial.net/sqlite-select/>
  - [Date And Time Functions](https://www.sqlite.org/lang_datefunc.html)
  - [Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
  - <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html>
  - [Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp)

### Learn further Python

- [Python List](https://www.programiz.com/python-programming/list)
- <https://docs.python.org/3/tutorial/venv.html>
- <https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files>
- <https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file>
- <https://docs.python.org/3/tutorial/errors.html>

### On Development Tools

- <https://quokkajs.com/docs/>
- <https://www.freecodecamp.org/news/git-diff-command/>
- <https://support.mozilla.org/en-US/kb/keyboard-shortcuts-thunderbird>

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
