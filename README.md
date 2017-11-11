# Phylab

phylab provides a set of utilities and interfaces to process laboratory data.

# How to use phylab

## On terminal

### 1. Use phylab.py
Use *python3* to interpret phylab.py, and specify the command and parameters, like this:
```
$ python3 phylab.py <command> <parameters>
```

Sometimes, the command requires input. We encourage you to save the data with separators in text file, and use *I/O redirection* to import as the input, like this:
```
$ python3 phylab.py <command> <parameters> < input.txt
```

Usually, phylab receives and outputs data or results in a certain format called Data and Text Compatibility Format(DTCF), which allows any other characters but only a pair of *angle brackets(<>)* containing the data separated by whitespaces. For example:
```
My data is as follows:
<2.50 7.45 8.03 10.2>
```
Detail information will appear in the output, but the final results are always displayed within a pair of *angle brackets(<>)*

You may doubt why we use such a strange way to show the results. In fact, we design this format to apply *pipe* feature to phylab.
When you want to process your data step by step, it is recommended that you use *pipe* to pass the previous result to the next command, like this:
```
$ python3 phylab.py <command_1> <parameters> < input.txt | <command_2> <parameters>
```
Phylab can retrieve the raw data from the complex output in this way.

Absolutely, you can take advantage of DTCF to attach some extra information alongside your raw data.

### 2. Use phylab.pyc
Simply run phylab.pyc and specify the command and parameters. All details are the same as above.

## On graphical user interface

### 1. Phylab Desktop
Phylab Desktop is available for Windows, MacOSX and Linux.
Download the installation package from the website and install phylab. Phylab provides various visual processing/editing tools, which helps you handle your laboratory data.

### 2. Phylab Online
Phylab is available for almost every current widely-used web browser.
Visit [Phylab Online](phylab online) and get started.

### 3. Phylab Mobile
Phylab is available for IOS and Android.
Download and install phylab on your mobile phone, process your laboratory data timely.

## Code by yourself

Phylab provides several modules and many mathmatical functions for end users. You can use these modules and functions to create your own applications, helping you deal with math problems and process laboratory data.
At present, phylab standard library only provides python interface, you may use *import* statement to import the module which you want to use. For example:
```
from Phylab.Core import CDataAnalysis
```

**Note: phylab is an unfinished project, any statements above are only plans**