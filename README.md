# OMR Checker

Read OMRs fast and accurately using a scanner 🖨 or your phone.

## What can OMRChecker do for me?

Once you configure the OMR layout, just throw images of the sheets at the software; and you'll get back the marked responses in an excel sheet!
### 1. Install global dependencies
To check if python3 and pip is already installed:

```bash
python --version
python -m pip --version
```

<details>
	<summary><b>Install Python3</b></summary>

To install python3 follow instructions [here](https://www.python.org/downloads/)

To install pip - follow instructions [here](https://pip.pypa.io/en/stable/installation/)

</details>
<details>
<summary><b>Install OpenCV</b></summary>

**Any installation method is fine.**

Recommended:

```bash
python -m pip install --user --upgrade pip
python -m pip install --user opencv-python
python -m pip install --user opencv-contrib-python
```

More details on pip install openCV [here](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/).

</details>

<details>

<summary><b>Extra steps(for Linux users only)</b></summary>


### 2. Install project dependencies

Clone the repo

```bash
git clone https://github.com/abdulhai1234/OMRchecker.git
cd OMRChecker/
```

Install pip requirements

```bash
python -m pip install --user -r requirements.txt
```

_**Note:** If you face a distutils error in pip, use `--ignore-installed` flag in above command._

<!-- Wiki should not get cloned -->

### 3. Run the code

1. First copy and examine the sample data to know how to structure your inputs:
   ```bash
   cp -r ./samples/sample1 inputs/
   # Note: you may remove previous inputs (if any) with `mv inputs/* ~/.trash`
   # Change the number N in sampleN to see more examples
   ```
2. Run OMRChecker:
   ```bash
   python main.py
   ```

Alternatively you can also use `python3 main.py -i ./samples/sample1`.

## OMRChecker for custom OMR Sheets

1. First, [create your own template.json](https://github.com/Udayraj123/OMRChecker/wiki/User-Guide).
2. Configure the tuning parameters.
3. Run OMRChecker with appropriate arguments (See full usage).
<!-- 4. Add answer key( TODO: add answer key/marking scheme guide)  -->

## Full Usage

```
python3 main.py [--setLayout] [--inputDir dir1] [--outputDir dir1]
```

Explanation for the arguments:

`--setLayout`: Set up OMR template layout - modify your json file and run again until the template is set.

`--inputDir`: Specify an input directory.

`--outputDir`: Specify an output directory.

<details>
<summary>
 <b>Deprecation logs</b>
</summary>

- The old `--noCropping` flag has been replaced with the 'CropPage' plugin in "preProcessors" of the template.json(see [samples](https://github.com/Udayraj123/OMRChecker/tree/master/samples)).
- The old `--autoAlign` flag can now be toggled from config.json
</details>

<!-- #### Testing the code
Datasets to test on :
Low Quality Dataset(For CV Based methods)) (1.5 GB)
Standard Quality Dataset(For ML Based methods) (3 GB)
High Quality Dataset(For custom processing) (6 GB)
-->


## FAQ

<details>
<summary>
<b>Why is this software free?</b>
</summary>

This project was born out of a student-led organization called as [Technothlon](https://technothlon.techniche.org.in). It is a logic-based international school championship organized by students of IIT Guwahati. Being a non-profit organization, and after seeing it work fabulously at such a large scale we decided to share this tool with the world. The OMR checking processes still involves so much tediousness which we aim to reduce dramatically.

We believe in the power of open source! Currently, OMRChecker is in an intermediate stage where only developers can use it. We hope to see it become more user-friendly as well as robust from exposure to different inputs from you all!

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

</details>

<details>
<summary>
<b>Can I use this code in my (public) work?</b>
</summary>

OMRChecker can be forked and modified. You are encouraged to play with it and we would love to see your own projects in action!

The only requirement is **disclose usage** of this software in your (public) code.

It is published under the [GPLv3 license](https://github.com/Udayraj123/OMRChecker/blob/master/LICENSE).

</details>

<details>
<summary>
<b>What are the ways to contribute?</b>
</summary>

<!-- - Help OMRChecker reach more people by giving a star! The Goal is to reach top position for the [OMR Topic](https://github.com/topics/omr) -->

- Join the developer community on [Discord](https://discord.gg/qFv2Vqf) to fix [issues](https://github.com/Udayraj123/OMRChecker/issues) with OMRChecker.

- If this project saved you large costs on OMR Software licenses, or saved efforts to make one. Consider donating an amount of your choice(donate section).

<!-- ![☕](https://miro.medium.com/fit/c/256/256/1*br7aoq_JVfxeg73x5tF_Sw.png) -->
<!-- [![paypal.me](https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Z5BNNK7AVFVH8&source=url) -->
<!-- https://www.amazon.in/hz/wishlist/ls/3V0TDQBI3T8IL -->

</details>

## Credits

_A Huge thanks to:_
_**Adrian Rosebrock** for his exemplary blog:_ https://pyimagesearch.com

_**Harrison Kinsley** aka sentdex for his [video tutorials](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq) and many other resources._

_**Satya Mallic** for his resourceful blog:_ https://www.learnopencv.com

_And to other amazing people from all over the globe who've made significant improvements in this project._

_Thank you!_

<!--
OpencV
matplotlib
some SO answers from roughworks
prof
-->
