# KataCR Detection Info

I'm gonna try to explain most of what I did here to make it easier to use. The implementation is very messy, so if you have any questions shoot me a DM on discord @avinashselvakumar. I'll probably improve it whenever I have more time. Contributions are more than welcome :)

# Changes from Original Detection
## Name Changes
The name of all the troops, buildings, ect. has changed.  They are all lowercase, and use kebab-case in their name. Ex.
* Mega Minion: `mega-minion`
* Goblin Barrel: `goblin-barrel`

## Additional Classes
Some more stuff is labeled in the KataCR detector. Nothing that was detected previously has been removed, but a lot of minor stuff is now labeled, including but not limited to:

* Emotes
* Skill activations (skeleton king summoning skeletons)
* Tower, building, & troop health bars (not including percentages)
* Deploy timers
* Evolution indicators (there is a small evolution icon that appears on the arena sometimes indicating whether the opponent has the evo or not)

## Screen Dimensions
This is probably the most important factor in the accuracy of the model. 

If you try to use this with the default screen dimensions, you'll quickly notice it isn't very accurate. I need to do some more experimenting with this, but there are two resolutions that I found work best (both on 320 DPI):

* 1080 x 1920
* 576 x 1024

If you are using a resolution other than 1080x2400 you need to modify the part{idx}_{ratio} in split_bbox_params in constant.py, where idx=1,2,3 represents the top-right corner time image position, the middle arena, and the bottom hand card area, respectively.

**If you are having problems with the accuracy, this is the first thing I would change**
# Setup
To install the requirements, assuming you have already completed the set up for ClashRoyaleBuildABot, you can simply run 

    pip install -r katacr_requirements.txt
This will install the requirements to run the model on CPU. For me, the speed on CPU was acceptable. However, I'm running a fairly high-end setup with the following specs:

CPU: 13th Gen Intel(R) Core(TM) i7-13700H   2.40 GHz (5 GHz turbo)
RAM: 16GB DDR5

If you would like to utilize a GPU, you can complete the setup using WSL and run the following command at the end:

    pip install jaxlib==0.4.26+cuda12.cudnn89 --force-reinstall

# Future Improvements
There are **a lot** of improvements to be made in this code. In this section, I have outlined two of the most major ones and some direction on where to begin to make these improvements. None of them should take very long to do, I just wanted to share this as soon as possible. If you do make the improvements, I kindly ask that you share them so that everyone can benefit :)

## Deleting unecessary files
To make this, I essentially took some of the code from an amazing repo called KataCR ([link](https://github.com/wty-yy/KataCR)) and used it here to identify troops. This repo was originally designed for a machine learning project with Clash Royale gameplay ([described here](https://github.com/wty-yy/KataCR/blob/master/README_en.md)), and as such contains a lot of files unrelated to the goal of this project. All the files that can be deleted safely are within the katacr folder. There probably is a smarter way to do this, but I would begin by tracing the requirements of everything within the katacr_detection folder and creating a list of required files. You could then delete everything else outside of that list.

## Identifying optimal screen dimensions
This is probably the more significant improvement on this list. The KataCR repo mentioned earlier uses videos of Clash Royale matches to gather data. In theory, whatever format these videos are in should be the ideal format. However, I haven't been able to figure out where the videos are. I found [this dataset](https://github.com/wty-yy/Clash-Royale-Replay-Dataset) used in KataCR, but it doesn't look like videos. The readme has a [section](https://github.com/wty-yy/KataCR/blob/master/README_en.md#model-verification) where he includes a note on the screen dimensions he used, but when I tested that it didn't work well. 

There also is an issue with filtering out unreasonable results (negative tile positions, ect.) but I have chosen not to include that here as that seems like a broader fix for ClashRoyaleBuildABot that should be brought up in the main repo.

