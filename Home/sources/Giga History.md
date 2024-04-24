NemeSys GigaSampler/GigaStudio
A brief history tracking the software and format


NemeSys (New Media Systems) Technology Inc., also known as NemeSys Music Technology, Inc., which we will refer to as NemeSys for the rest of this text, was a company founded in 1996. It was dedicated to build software-based digital signal processing products and technologies, by bringing together major host-based signal processing technology developers. Jim Van Buskirk was probably the initial developer for the idea, a core developer for GigaSampler, and driving force for the usage of this technology.
https://web.archive.org/web/19980131224657/http://www.nemesysmusic.com/nemehist.htm
https://web.archive.org/web/19980131225824/http://www.nemesysmusic.com/pr_eastwest.htm
https://www.linkedin.com/in/jimvanbuskirk


While the website suggests a whole host of products, this article will review the history of the Giga Technology.
Additionally, GigaSampler (TM) will be referred to as GigaSampler. The term GigaSampler may also be used to refer to GigaStudio (TM), or the Giga Technology itself. One may consider intention contextual or non-definite.


The GigaSampler technology is said to have been unveiled at the NAMM Convention in 1998. NemeSys teamed up with EastWest Studios to unveil it. I cannot find any sources other than the GigaSampler site archive itself to indicate whether this actually happened. The NAMM International Music Market in 1998 occurred between January 29 and February 1.
An exclusive relationship between Doug Rogers (founder of EastWest Sounds) and NemeSys (described "Van Buskirk's NemeSys," a possible indicator of his role in figureheading this technology) was what produced in 1997 the GigaSampler software. EastWest sounds was initially the sole distributor of GigaSampler.
https://web.archive.org/web/19980131225824/http://www.nemesysmusic.com/pr_eastwest.htm
https://www.soundonsound.com/music-business/eastwest-man-behind-brand


GigaSampler, then, was a proprietary software sampler developed by NemeSys Music Technology. It represented a major milestone in sampling architecture and by extension music quality. It was revolutionary in that, instead of sampling and saving a base small version of an instrument and generate dynamics as required, it enabled sampling all dynamics of an instrument and control output as required. This resulted in less demand of dynamic emulation, freeing up RAM, and the additional result of a rich, higher quality (at the time) sound, due to dynamics being recorded instead of generated.
These dynamics are called dimensions, and they are properties of an instrument's sound that enable its characteristics to be modulated as per the input to produce an expressive note.
Examples of dimensions include velocity layering, microphone position, sustain/release pedals, etc.
https://www.soundonsound.com/reviews/nemesys-gigasampler-v15


On January 16, 1997 (16/01/1997), an EastWest press release covered the release of the GigaSampler at NAMM (notice the specific date and the range of dates of the NAMM market: I do not know where the disparity is from). Some information on what it was said to represent has been given.
GigaSampler was said to represent "the most fundamental advance in music sampling architecture since the advent of [Analogue/Digital] conversion".
It was said to be capable of "sampled musical instrument quality, the likes of which have never been achieved by any commercial sampler at any price".
It did this by utilizing "behaviorial sampling," which saved RAM memory space.
Most samplers contained instrument samples that were compressed, filtered, and looped, to be in the simplest form possible and save memory space. This was because of dimensions (a set of dynamic demands on a sample that modulate the realtime playback and characteristics of a sound based on modulation). Degrading the quality of the sample to the least expressive possible (through filtering, compression, looping, etc) went hand-in-hand with subsequently applying demands on the sound based on requirements. This meant an enormous project on a DSP level to simulate the behaviour of dynamics, and it also meant a large RAM consumption. Samplers would run entirely in the RAM and end up occupying all RAM available, forcing samplers to run on basic small minimum-quality sounds alongside a large dynamic generation.
The GigaSampler discarded the memory barrier and used minimal realtime re-creation of dynamics by enabling the instrument itself to be sampled with its dynamics, storing the sample sets in dimensions, and allowing the user to assign instrument controllers to these dimensions to manage them, allowing dynamic control.
These dimensions were stored as samples in the hard disk (as opposed to emulated using the RAM), allowing a larger size of instrument.
Modern technologies and standards, such as the Soundfont 2 standard, achieve the behaviour by using a process called articulation, accessible by modulators.
It was said to be "the only sampler capable of handling instruments as large as the size of your hard disk [...] by using hard disks instead of RAM for primary instrument sample access [...] ."
https://web.archive.org/web/19980131224231/http://www.nemesysmusic.com/namm98.htm
https://web.archive.org/web/19980131224041/http://www.nemesysmusic.com/gs.htm
https://web.archive.org/web/19980131224231/http://www.nemesysmusic.com/pr_eastwest.htm


On February 3, 2000, NemeSys announced GigaStudio, the successor of GigaSampler. GigaStudio was also said to use the patented EndlessWave (TM) technology, trademark of Comexant systems.
It came with support for higher MIDI and layering capability, and several additional features and utilities.
https://web.archive.org/web/20011217133926/http://www.nemesysmusic.com/news/releases/000203.html
https://web.archive.org/web/20020203161712/http://www.harmony-central.com/Newp/WNAMM00/NemeSys/GigaStudio.html
https://web.archive.org/web/20011217133926/http://www.nemesysmusic.com/news/releases/000203.html
https://web.archive.org/web/20020202164926fw_/http://www.nemesysmusic.com/products/gigacompare.html


On July 18 2001, TASCAM purchased the NemeSys company and began redistributing under its brand name GigaSampler and GigaStudio.
https://web.archive.org/web/20020124230610/http://www.nemesysmusic.com/
https://web.archive.org/web/20020210121014/http://tascam.com/press/hot_news/nemesys/index.php
https://web.archive.org/web/20020205043946/http://www.tascam.com/press/news/2001_07/1_nemesys.html


On July 21, 2008, TASCAM ceased development of GigaStudio.
https://www.soundonsound.com/news/tascam-cease-development-gigastudio


On April 1, 2009, the Giga Technology and trademark were said to have purchased by Gary Garritan. Garritan Company acquired it.
https://www.soundonsound.com/techniques/will-gigasampler-make-comeback
https://www.garritan.com/blog/


The GigaSampler uses gig instruments, their file format having the extension ".gig". Multiple instruments can be in one file, by placing them in different MIDI patches of the same bank.
MIDI bank number may have been utilised in assigning instruments to channels, and performance files (".prf," ".gsp") appear to be macros that load instruments into these MIDI channels.
https://tascam.com/downloads/tascam/508/gs3_editor_manual.pdf
https://www.chickensys.com/support/software/translator/giga/index.html