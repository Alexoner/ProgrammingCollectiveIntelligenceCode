<div id="article_content" class="article_content">

<p align="center"><strong><span style="font-size:18px">计算机视觉、机器学习相关领域论文和源代码大集合…</span></strong></p>
<p align="center"><a href="mailto:zouxy09@qq.com"><span style="font-size:18px; color:#0000ff">zouxy09@qq.com</span></a></p>
<p align="center"><a href="http://blog.csdn.net/zouxy09"><span style="font-size:18px; color:#0000ff">http://blog.csdn.net/zouxy09</span></a></p>
<p align="left"><span style="font-size:18px; color:#555555">&nbsp;</span></p>
<p align="left"><span style="font-size:18px"><span style="color:red">注：下面有</span><span style="color:red">project</span><span style="color:red">网站的大部分都有</span><span style="color:red">paper</span><span style="color:red">和相应的</span><span style="color:red">code</span><span style="color:red">。</span><span style="color:red">Code</span><span style="color:red">一般是</span><span style="color:red">C/C++</span><span style="color:red">或者</span><span style="color:red">Matlab</span><span style="color:red">代码。</span></span></p>
<p align="left"><span style="font-size:18px; color:#ff0000">最近一次更新：2013-3-17</span></p>
<p align="left"><span style="color:#555555"><span style="font-size:14px"><br>
</span></span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">一、特征提取Feature Extraction：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">SIFT [1] [<a href="http://www.cs.ubc.ca/~lowe/keypoints/siftDemoV4.zip"><span style="color:#2970a6">Demo program</span></a>][<a href="http://blogs.oregonstate.edu/hess/code/sift/"><span style="color:#2970a6">SIFT Library</span></a>]
 [<a href="http://www.vlfeat.org/"><span style="color:#2970a6">VLFeat</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">PCA-SIFT [2] [<a href="http://www.cs.cmu.edu/~yke/pcasift/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Affine-SIFT [3] [<a href="http://www.ipol.im/pub/algo/my_affine_sift/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">SURF [4] [<a href="http://www.chrisevansdev.com/computer-vision-opensurf.html"><span style="color:#2970a6">OpenSURF</span></a>] [<a href="http://www.maths.lth.se/matematiklth/personal/petter/surfmex.php"><span style="color:#2970a6">Matlab
 Wrapper</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Affine Covariant Features [5] [<a href="http://www.robots.ox.ac.uk/~vgg/research/affine/"><span style="color:#2970a6">Oxford project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">MSER [6] [<a href="http://www.robots.ox.ac.uk/~vgg/research/affine/"><span style="color:#2970a6">Oxford project</span></a>] [<a href="http://www.vlfeat.org/"><span style="color:#2970a6">VLFeat</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Geometric Blur [7] [<a href="http://www.robots.ox.ac.uk/~vgg/software/MKL/"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Local Self-Similarity Descriptor [8] [<a href="http://www.robots.ox.ac.uk/~vgg/software/SelfSimilarity/"><span style="color:#2970a6">Oxford implementation</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Global and Efficient Self-Similarity [9] [<a href="http://www.vision.ee.ethz.ch/~calvin/gss/selfsim_release1.0.tgz"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Histogram of Oriented Graidents [10] [<a href="http://www.navneetdalal.com/software"><span style="color:#2970a6">INRIA Object Localization Toolkit</span></a>] [<a href="http://www.computing.edu.au/~12482661/hog.html"><span style="color:#2970a6">OLT
 toolkit for Windows</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">GIST [11] [<a href="http://people.csail.mit.edu/torralba/code/spatialenvelope/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Shape Context [12] [<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/sc_digits.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Color Descriptor [13] [<a href="http://koen.me/research/colordescriptors/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Pyramids of Histograms of Oriented Gradients [<a href="http://www.robots.ox.ac.uk/~vgg/research/caltech/phog/phog.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Space-Time Interest Points (STIP) [14][<a href="http://www.nada.kth.se/cvap/abstracts/cvap284.html"><span style="color:#0000ff">Project</span></a>] [<a href="http://www.irisa.fr/vista/Equipe/People/Laptev/download/stip-1.1-winlinux.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Boundary Preserving Dense Local Regions [15][<a href="http://vision.cs.utexas.edu/projects/bplr/bplr.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Weighted Histogram[<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/whistc.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Histogram-based Interest Points Detectors[<a href="http://www.cs.nthu.edu.tw/~htchen/hipd_cvpr09.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://740-2.cs.nthu.edu.tw/~htchen/hipd/hist_corner.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">An OpenCV - C++ implementation of Local Self Similarity Descriptors [<a href="http://intuitionlogic.com/post/2011/04/11/A-OpenCV-C++-implementation-of-Local-Self-Similarity-Descriptors.aspx"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Fast Sparse Representation with Prototypes[<a href="http://faculty.ucmerced.edu/mhyang/cvpr10_fsr.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Corner Detection [<a href="http://kiwi.cs.dal.ca/~dparks/CornerDetection/index.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">AGAST Corner Detector: faster than FAST and even FAST-ER[<a href="http://www6.in.tum.de/Main/ResearchAgast"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Real-time Facial Feature Detection using Conditional Regression Forests[<a href="http://files.is.tue.mpg.de/jgall/projects/facialfeatures/facialfeatures.html"><span style="color:rgb(0,0,255)">Project</span></a>]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Global and Efficient Self-Similarity for Object Classification and Detection[<a href="http://groups.inf.ed.ac.uk/calvin/gss/selfsim_release1.0.tgz">code</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>WαSH: Weighted α-Shapes for Local Feature Detection[<a href="http://image.ntua.gr/iva/research/wash/">Project</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>HOG[<a href="http://soc.fudan.edu.cn/vip/projects/gradproj/wiki/HOG%E4%BB%A3%E7%A0%81">Project</a>]</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Online Selection of Discriminative Tracking Features[<a href="http://www.cs.ucla.edu/~roozbehm/cs7495/report.html">Project</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">二、图像分割Image Segmentation：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Normalized Cut [1] [<a href="http://www.cis.upenn.edu/~jshi/software/"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Gerg Mori’ Superpixel code [2] [<a href="http://www.cs.sfu.ca/~mori/research/superpixels/"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Efficient Graph-based Image Segmentation [3] [<a href="http://people.cs.uchicago.edu/~pff/segment/"><span style="color:#2970a6">C++ code</span></a>] [<a href="http://www.mathworks.com/matlabcentral/fileexchange/25866-efficient-graph-based-image-segmentation"><span style="color:#2970a6">Matlab
 wrapper</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Mean-Shift Image Segmentation [4] [<a href="http://coewww.rutgers.edu/riul/research/code/EDISON/index.html"><span style="color:#2970a6">EDISON C++ code</span></a>] [<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/edison_matlab_interface.tar.gz"><span style="color:#2970a6">Matlab
 wrapper</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">OWT-UCM Hierarchical Segmentation [5] [<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html"><span style="color:#2970a6">Resources</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Turbepixels [6] [<a href="http://www.cs.toronto.edu/~babalex/turbopixels_code.tar.gz"><span style="color:#2970a6">Matlab code 32bit</span></a>] [<a href="http://www.cs.toronto.edu/~babalex/TurboPixels64.rar"><span style="color:#2970a6">Matlab
 code 64bit</span></a>] [<a href="http://www.cs.toronto.edu/~babalex/superpixels_update.tgz"><span style="color:#2970a6">Updated code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Quick-Shift [7] [<a href="http://www.vlfeat.org/overview/quickshift.html"><span style="color:#2970a6">VLFeat</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">SLIC Superpixels [8] [<a href="http://ivrgwww.epfl.ch/supplementary_material/RK_SLICSuperpixels/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Segmentation by Minimum Code Length [9] [<a href="http://perception.csl.uiuc.edu/coding/image_segmentation/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Biased Normalized Cut [10] [<a href="http://www.cs.berkeley.edu/~smaji/projects/biasedNcuts/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Segmentation Tree [11-12] [<a href="http://vision.ai.uiuc.edu/segmentation"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Entropy Rate Superpixel Segmentation [13] [<a href="http://www.umiacs.umd.edu/~mingyliu/src/ers_matlab_wrapper_v0.1.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Fast Approximate Energy Minimization via Graph Cuts[<a href="http://www.csd.uwo.ca/faculty/olga/Papers/pami01_final.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://vision.csd.uwo.ca/code/gco-v3.0.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Efﬁcient Planar Graph Cuts with Applications in Computer Vision[<a href="http://www.csd.uwo.ca/~schmidtf/pdf/schmidt_et_al_cvpr09.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://vision.csd.uwo.ca/code/PlanarCut-v1.0.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Isoperimetric Graph Partitioning for Image Segmentation[<a href="http://www.cns.bu.edu/~lgrady/grady2006isoperimetric.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.cns.bu.edu/~lgrady/grady2006isoperimetric_code.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Random Walks for Image Segmentation[<a href="http://www.cns.bu.edu/~lgrady/grady2006random.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.cns.bu.edu/~lgrady/random_walker_matlab_code.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Blossom V: A new implementation of a minimum cost perfect matching algorithm[<a href="http://pub.ist.ac.at/~vnk/software/blossom5-v2.03.src.tar.gz%20%20http:/pub.ist.ac.at/~vnk/software/blossom5-v2.03.src.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">An Experimental Comparison of Min-Cut/Max-Flow Algorithms for Energy Minimization in Computer Vision[<a href="http://www.csd.uwo.ca/~yuri/Papers/pami04.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://pub.ist.ac.at/~vnk/software/maxflow-v3.01.src.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Geodesic Star Convexity for Interactive Image Segmentation[<a href="http://www.robots.ox.ac.uk/~vgg/software/iseg/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Contour Detection and Image Segmentation Resources[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html"><span style="color:#0000ff">Project</span></a>][<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_source.tgz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Biased Normalized Cuts[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/biasedNcuts/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Max-flow/min-cut[<a href="http://vision.csd.uwo.ca/code/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Chan-Vese Segmentation using Level Set[<a href="http://www.ipol.im/pub/art/2012/g-cv/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Toolbox of Level Set Methods[<a href="http://www.cs.ubc.ca/~mitchell/ToolboxLS/index.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Re-initialization Free Level Set Evolution via Reaction Diffusion[<a href="http://www4.comp.polyu.edu.hk/~cslzhang/RD/RD.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Improved C-V active contour model[<a href="http://www4.comp.polyu.edu.hk/~cskhzhang/J_papers/ICV.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www4.comp.polyu.edu.hk/~cskhzhang/J_papers/ICV.rar"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Variational Multiphase Level Set Approach to Simultaneous Segmentation and Bias Correction[<a href="http://www4.comp.polyu.edu.hk/~cskhzhang/J_papers/ICIP10_SVMLS.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www4.comp.polyu.edu.hk/~cskhzhang/J_papers/SVMLS_v0.rar"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Level Set Method Research by Chunming Li[<a href="http://www.engr.uconn.edu/~cmli/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style="color:rgb(85,85,85)">ClassCut for Unsupervised Class Segmentation[</span><a href="http://groups.inf.ed.ac.uk/calvin/classcut/ClassCut-release_v1.0.zip">cod</a>e<span style="color:rgb(85,85,85)">]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>SEEDS: Superpixels Extracted via Energy-Driven Sampling
<a href="http://www.vision.ee.ethz.ch/~vamichae/seeds/">[Project</a>][<a href="http://www.mvdblive.org/seeds/">other</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">三、目标检测Object Detection：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A simple object detector with boosting [<a href="http://people.csail.mit.edu/torralba/shortCourseRLOC/boosting/boosting.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">INRIA Object Detection and Localization Toolkit [1] [<a href="http://pascal.inrialpes.fr/soft/olt/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Discriminatively Trained Deformable Part Models [2] [<a href="http://people.cs.uchicago.edu/~pff/latent/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Cascade Object Detection with Deformable Part Models [3] [<a href="http://people.cs.uchicago.edu/~rbg/star-cascade/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Poselet [4] [<a href="http://www.eecs.berkeley.edu/~lbourdev/poselets/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Implicit Shape Model [5] [<a href="http://www.vision.ee.ethz.ch/~bleibe/code/ism.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Viola and Jones’s Face Detection [6] [<a href="http://pr.willowgarage.com/wiki/Face_detection"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Bayesian Modelling of Dyanmic Scenes for Object Detection[<a href="http://vision.eecs.ucf.edu/papers/01512057.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://vision.eecs.ucf.edu/Code/Background.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Hand detection using multiple proposals[<a href="http://www.robots.ox.ac.uk/~vgg/software/hands/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Color Constancy, Intrinsic Images, and Shape Estimation[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/reconstruction/BarronMalikECCV2012.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.cs.berkeley.edu/~barron/BarronMalikECCV2012_code.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Discriminatively trained deformable part models[<a href="http://people.cs.uchicago.edu/~rbg/latent/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Gradient Response Maps for Real-Time Detection of Texture-Less Objects: LineMOD [<a href="http://campar.cs.tum.edu/Main/StefanHinterstoisser"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Image Processing On Line[<a href="http://www.ipol.im/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Robust Optical Flow Estimation[<a href="http://www.ipol.im/pub/pre/21/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Where's Waldo: Matching People in Images of Crowds[<a href="http://homes.cs.washington.edu/~rahul/data/WheresWaldo.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Scalable Multi-class Object Detection[<a href="http://files.is.tue.mpg.de/jgall/projects/houghMC/houghMC.html"><span style="color:rgb(0,0,255)">Project</span></a>]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Class-Specific Hough Forests for Object Detection[<a href="http://files.is.tue.mpg.de/jgall/projects/houghforest/houghforest.html"><span style="color:rgb(0,0,255)">Project</span></a>]</span><br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Deformed Lattice Detection In Real-World Images[<a href="http://vision.cse.psu.edu/data/data.shtml">Project</a>]<br>
</span></span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Discriminatively trained deformable part models[<a href="http://people.cs.uchicago.edu/~rbg/latent/">Project</a>]<br>
</span></span></span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">四、显著性检测Saliency Detection：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Itti, Koch, and Niebur’ saliency detection [1] [<a href="http://www.saliencytoolbox.net/"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Frequency-tuned salient region detection [2] [<a href="http://ivrgwww.epfl.ch/supplementary_material/RK_CVPR09/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Saliency detection using maximum symmetric surround [3] [<a href="http://ivrg.epfl.ch/supplementary_material/RK_ICIP2010/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Attention via Information Maximization [4] [<a href="http://www.cse.yorku.ca/~neil/AIM.zip"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Context-aware saliency detection [5] [<a href="http://webee.technion.ac.il/labs/cgm/Computer-Graphics-Multimedia/Software/Saliency/Saliency.html"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Graph-based visual saliency [6] [<a href="http://www.klab.caltech.edu/~harel/share/gbvs.php"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Saliency detection: A spectral residual approach. [7] [<a href="http://www.klab.caltech.edu/~xhou/projects/spectralResidual/spectralresidual.html"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Segmenting salient objects from images and videos. [8] [<a href="http://www.cse.oulu.fi/MVG/Downloads/saliency"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Saliency Using Natural statistics. [9] [<a href="http://cseweb.ucsd.edu/~l6zhang/"><span style="color:#2970a6">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Discriminant Saliency for Visual Recognition from Cluttered Scenes. [10] [<a href="http://www.svcl.ucsd.edu/projects/saliency/"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Learning to Predict Where Humans Look [11] [<a href="http://people.csail.mit.edu/tjudd/WherePeopleLook/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Global Contrast based Salient Region Detection [12] [<a href="http://cg.cs.tsinghua.edu.cn/people/~cmm/saliency/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Bayesian Saliency via Low and Mid Level Cues[<a href="http://ice.dlut.edu.cn/lu/Project/TIP_scm/TIP_scm.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Top-Down Visual Saliency via Joint CRF and Dictionary Learning[<a href="http://faculty.ucmerced.edu/mhyang/papers/cvpr12a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/top-down-saliency.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Saliency Detection: A Spectral Residual Approach[<a href="http://www.klab.caltech.edu/~xhou/projects/dva/dva.html">Code</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">五、图像分类、聚类Image Classification, Clustering</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Pyramid Match [1] [<a href="http://people.csail.mit.edu/jjl/libpmk/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Spatial Pyramid Matching [2] [<a href="http://www.cs.unc.edu/~lazebnik/research/SpatialPyramid.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Locality-constrained Linear Coding [3] [<a href="http://www.ifp.illinois.edu/~jyang29/LLC.htm"><span style="color:#2970a6">Project</span></a>] [<a href="http://www.ifp.illinois.edu/~jyang29/codes/CVPR10-LLC.rar"><span style="color:#2970a6">Matlab
 code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Sparse Coding [4] [<a href="http://www.ifp.illinois.edu/~jyang29/ScSPM.htm"><span style="color:#2970a6">Project</span></a>] [<a href="http://www.ifp.illinois.edu/~jyang29/codes/CVPR09-ScSPM.rar"><span style="color:#2970a6">Matlab
 code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Texture Classification [5] [<a href="http://www.robots.ox.ac.uk/~vgg/research/texclass/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Multiple Kernels for Image Classification [6] [<a href="http://www.robots.ox.ac.uk/~vgg/software/MKL/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Feature Combination [7] [<a href="http://www.vision.ee.ethz.ch/~pgehler/projects/iccv09/index.html"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">SuperParsing [<a href="http://www.cs.unc.edu/~jtighe/Papers/ECCV10/eccv10-jtighe-code.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Large Scale Correlation Clustering Optimization[<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/LargeScaleCC1.0.tar.gz"><span style="color:#0000ff">Matlab code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Detecting and Sketching the Common[<a href="http://www.wisdom.weizmann.ac.il/~vision/SketchTheCommon"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Self-Tuning Spectral Clustering[<a href="http://www.vision.caltech.edu/lihi/Demos/SelfTuningClustering.html"><span style="color:#0000ff">Project</span></a>][<a href="http://www.vision.caltech.edu/lihi/Demos/SelfTuning/ZPclustering.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">User Assisted Separation of Reflections from a Single Image Using a Sparsity Prior[<a href="http://www.wisdom.weizmann.ac.il/~levina/papers/assisted-eccv04.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.wisdom.weizmann.ac.il/~levina/papers/reflections.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Filters for Texture Classification[<a href="http://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html#download"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Multiple Kernel Learning for Image Classification[<a href="http://www.robots.ox.ac.uk/~vgg/software/MKL/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>SLIC Superpixels[<a href="http://ivrg.epfl.ch/supplementary_material/RK_SLICSuperpixels/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">六、抠图Image Matting</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Closed Form Solution to Natural Image Matting [<a href="http://people.csail.mit.edu/alevin/matting.tar.gz"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Spectral Matting [<a href="http://www.vision.huji.ac.il/SpectralMatting/"><span style="color:#2970a6">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Learning-based Matting [<a href="http://www.mathworks.com/matlabcentral/fileexchange/31412"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><strong><span style="font-size:14px">&nbsp;</span></strong></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">七、目标跟踪Object Tracking：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Forest of Sensors - Tracking Adaptive Background Mixture Models [<a href="http://www.ai.mit.edu/projects/vsam/Tracking/index.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Object Tracking via Partial Least Squares Analysis[<a href="http://faculty.ucmerced.edu/mhyang/papers/tip12_pls_tracking.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/PLS_tracker_tip.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Robust Object Tracking with Online Multiple Instance Learning[<a href="http://faculty.ucmerced.edu/mhyang/papers/pami11b.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://vision.ucsd.edu/~bbabenko/project_miltrack.shtml"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Online Visual Tracking with Histograms and Articulating Blocks[<a href="http://www.cise.ufl.edu/~smshahed/tracking.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Incremental Learning for Robust Visual Tracking[<a href="http://www.cs.toronto.edu/~dross/ivt/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Real-time Compressive Tracking[<a href="http://www4.comp.polyu.edu.hk/~cslzhang/CT/CT.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Robust Object Tracking via Sparsity-based Collaborative Model[<a href="http://faculty.ucmerced.edu/mhyang/project/cvpr12_scm.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Visual Tracking via Adaptive Structural Local Sparse Appearance Model[<a href="http://faculty.ucmerced.edu/mhyang/project/cvpr12_jia_project.htm"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Online Discriminative Object Tracking with Local Sparse Representation[<a href="http://faculty.ucmerced.edu/mhyang/papers/wacv12a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/wacv12a_code.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Superpixel Tracking[<a href="http://faculty.ucmerced.edu/mhyang/papers/iccv11a.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Learning Hierarchical Image Representation with Sparsity, Saliency and Locality[<a href="http://faculty.ucmerced.edu/mhyang/papers/bmvc11a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/BMVC11-HSSL-package.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Online Multiple Support Instance Tracking [<a href="http://faculty.ucmerced.edu/mhyang/papers/fg11a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/fg11_omsit.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Visual Tracking with Online Multiple Instance Learning[<a href="http://vision.ucsd.edu/~bbabenko/project_miltrack.shtml"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Object detection and recognition[<a href="http://c2inet.sce.ntu.edu.sg/Jianxin/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Compressive Sensing Resources[<a href="http://dsp.rice.edu/cs"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Robust Real-Time Visual Tracking using Pixel-Wise Posteriors[<a href="http://www.robots.ox.ac.uk/~cbibby/index.shtml"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Tracking-Learning-Detection[<a href="http://info.ee.surrey.ac.uk/Personal/Z.Kalal/"><span style="color:#0000ff">Project</span></a>][<a href="https://github.com/arthurv/OpenTLD"><span style="color:#0000ff">OpenTLD/C++ Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>the HandVu：vision-based hand gesture interface[<a href="http://ilab.cs.ucsb.edu/index.php/component/content/article/12/29">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Learning Probabilistic Non-Linear Latent Variable Models for Tracking Complex Activities<span style="color:rgb(85,85,85)">[</span><a href="http://files.is.tue.mpg.de/jgall/projects/stochGPLVM/stochGPLVM.html" style="">Project</a><span style="color:rgb(85,85,85)">]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">八、Kinect：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Kinect toolbox[<a href="http://kinecttoolbox.codeplex.com/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">OpenNI[<a href="http://www.openni.org/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">zouxy09 CSDN Blog[<a href="http://blog.csdn.net/zouxy09/article/details/8145688"><span style="color:#0000ff">Resource</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">FingerTracker 手指跟踪[</span><span style=""><span style="color:#0000ff"><a href="http://makematics.com/code/FingerTracker/">code</a></span><span style="color:#555555">]</span></span><br>
</p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">九、3D相关：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">3D Reconstruction of a Moving Object[<a href="http://www.wisdom.weizmann.ac.il/~ronen/papers/Simakov%20Frolova%20Basri%20-%20Dense%20Shape%20Reconstruction%20Under%20Arbitrary%20Unknown%20Lighting.pdf"><span style="color:#0000ff">Paper</span></a>]
 [<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/SFB_matlab1.0.tar.gz"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Shape From Shading Using Linear Approximation[<a href="http://vision.eecs.ucf.edu/shadsrc.html"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Combining Shape from Shading and Stereo Depth Maps[<a href="http://vision.eecs.ucf.edu/combsrc.html"><span style="color:#0000ff">Project</span></a>][<a href="http://vision.eecs.ucf.edu/projects/ShapeFromShading/combine.tar.Z"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Shape from Shading: A Survey[<a href="http://vision.eecs.ucf.edu/papers/shah/99/ZTCS99.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://vision.eecs.ucf.edu/projects/ShapeFromShading/SFS_Survey_1_00.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Spatio-Temporal Descriptor based on 3D Gradients (HOG3D)[<a href="http://lear.inrialpes.fr/people/klaeser/research_hog3d"><span style="color:#0000ff">Project</span></a>][<a href="http://lear.inrialpes.fr/people/klaeser/software_3d_video_descriptor"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Multi-camera Scene Reconstruction via Graph Cuts[<a href="http://www.cs.cornell.edu/~rdz/papers/kz-eccv02-recon.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://pub.ist.ac.at/~vnk/software/match-v3.4.src.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">A Fast Marching Formulation of Perspective Shape from Shading under Frontal Illumination[<a href="http://www.cs.ucf.edu/~vision"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.ee.cityu.edu.hk/~syyuen/Public/SfS/PRL_Perspective_FMM.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Reconstruction:3D Shape, Illumination, Shading, Reflectance, Texture[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/reconstruction/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Monocular Tracking of 3D Human Motion with a Coordinated Mixture of Factor Analyzers[<a href="http://faculty.ucmerced.edu/mhyang/code/PackagedTrackingCode.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Learning 3-D Scene Structure from a Single Still Image[<a href="http://ai.stanford.edu/~asaxena/reconstruction3d/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">十、机器学习算法：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Matlab class for computing Approximate Nearest Nieghbor (ANN) [<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/ann_wrapper_Mar2012.tar.gz"><span style="color:#0000ff">Matlab class</span></a> providing interface to<a href="http://www.cs.umd.edu/~mount/ANN/"><span style="color:#0000ff">ANN
 library</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Random Sampling[<a href="http://www.wisdom.weizmann.ac.il/~bagon/matlab_code/weight_sample.tar.gz"><span style="color:#0000ff">code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Probabilistic Latent Semantic Analysis (pLSA)[<a href="http://www.robots.ox.ac.uk/~vgg/software/pLSA/pLSA_demo.tgz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">FASTANN and FASTCLUSTER for approximate k-means (AKM)[<a href="http://www.robots.ox.ac.uk/~vgg/software/fastann/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Fast Intersection / Additive Kernel SVMs[<a href="http://www.cs.berkeley.edu/~smaji/projects/fiksvm/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">SVM[<a href="http://osmot.cs.cornell.edu/svm_light/"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Ensemble learning[<a href="http://c2inet.sce.ntu.edu.sg/Jianxin/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Deep Learning[<a href="http://deeplearning.net/"><span style="color:#0000ff">Net</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>Deep Learning Methods for Vision[<a href="http://cs.nyu.edu/~fergus/tutorials/deep_learning_cvpr12/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Neural Network for Recognition of Handwritten Digits[<a href="http://www.codeproject.com/KB/library/NeuralNetRecognition.aspx"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Training a deep autoencoder or a classifier on MNIST digits[<a href="http://www.cs.toronto.edu/~hinton/MatlabForSciencePaper.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>THE MNIST DATABASE of handwritten digits[<a href="http://yann.lecun.com/exdb/mnist/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Ersatz：deep neural networks in the cloud[<a href="http://www.ersatz1.com/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Deep Learning [<a href="http://www.cs.nyu.edu/~yann/research/deep/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>sparseLM : Sparse Levenberg-Marquardt nonlinear least squares in C/C++[<a href="http://www.ics.forth.gr/~lourakis/sparseLM/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Weka 3: Data Mining Software in Java[<a href="http://www.cs.waikato.ac.nz/ml/weka/">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Invited talk "A Tutorial on Deep Learning" by Dr. Kai Yu (余凯)[<a href="http://vipl.ict.ac.cn/News/academic-report-tutorial-deep-learning-dr-kai-yu">Video</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>CNN - Convolutional neural network class[<a href="http://www.mathworks.cn/matlabcentral/fileexchange/24291">Matlab Tool</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Yann LeCun's Publications[<a href="http://yann.lecun.com/exdb/publis/index.html#lecun-98">Wedsite</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>LeNet-5, convolutional neural networks[<a href="http://yann.lecun.com/exdb/lenet/index.html">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>Training a deep autoencoder or a classifier on MNIST digits[<a href="http://www.cs.toronto.edu/~hinton/MatlabForSciencePaper.html">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style="color:rgb(85,85,85)">Deep Learning 大牛</span>Geoffrey E. Hinton<span style="color:rgb(85,85,85)">'s HomePage[<a href="http://www.cs.toronto.edu/~hinton/">Website</a>]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Multiple Instance Logistic Discriminant-based Metric Learning (MildML) and Logistic Discriminant-based
 Metric Learning (LDML)[<a href="http://lear.inrialpes.fr/people/guillaumin/code.php#mildml">Code</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Sparse coding simulation software[<a href="http://redwood.berkeley.edu/bruno/sparsenet/">Project</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Visual Recognition and Machine Learning Summer School[<a href="http://lear.inrialpes.fr/software">Software</a>]<br>
</span></span></p>
<p align="left" style="background:white"><strong><span style="font-size:14px">&nbsp;</span></strong></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">十一、目标、行为识别Object, Action Recognition：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Action Recognition by Dense Trajectories[<a href="http://lear.inrialpes.fr/people/wang/dense_trajectories"><span style="color:#0000ff">Project</span></a>][<a href="http://lear.inrialpes.fr/people/wang/download/dense_trajectory_release.tar.gz"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Action Recognition Using a Distributed Representation of Pose and Appearance[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/action/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Recognition Using Regions[<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/glam-cvpr09.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.eecs.berkeley.edu/Research/Projects/CS/vision/shape/glam_cvpr09_v2.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">2D Articulated Human Pose Estimation[<a href="http://www.vision.ee.ethz.ch/~calvin/articulated_human_pose_estimation_code/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Fast Human Pose Estimation Using Appearance and Motion via Multi-Dimensional Boosting Regression[<a href="http://faculty.ucmerced.edu/mhyang/papers/cvpr07a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://www.cise.ufl.edu/~smshahed/cvpr07_fast_human_pose.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Estimating Human Pose from Occluded Images[<a href="http://faculty.ucmerced.edu/mhyang/papers/accv09a.pdf"><span style="color:#0000ff">Paper</span></a>][<a href="http://faculty.ucmerced.edu/mhyang/code/accv09_pose.zip"><span style="color:#0000ff">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Quasi-dense wide baseline matching[<a href="http://www.ee.oulu.fi/~jkannala/quasidense/quasidense.html"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>ChaLearn Gesture Challenge:&nbsp;Principal motion: PCA-based reconstruction of motion histograms[<a href="http://gesture.chalearn.org/data/sample-code">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Real Time Head Pose Estimation with Random Regression Forests[</span><a href="http://files.is.tue.mpg.de/jgall/projects/RFhead/RFhead.html" style="">Project</a><span style="color:rgb(85,85,85)">]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">2D Action Recognition Serves 3D Human Pose Estimation[</span><a href="http://files.is.tue.mpg.de/jgall/projects/ARforPose/ARforPose.html">Project<span style="color:rgb(85,85,85)">]</span></a><br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">A Hough Transform-Based Voting Framework for Action Recognition[</span><a href="http://files.is.tue.mpg.de/jgall/projects/houghAR/houghAR.html" style="">Project<span style="color:rgb(85,85,85)">]</span></a><br>
</span></p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Motion Interchange Patterns for Action Recognition in Unconstrained Videos<span style="color:rgb(85,85,85)">[</span><a href="http://www.openu.ac.il/home/hassner/projects/MIP/" style="">Project<span style="color:rgb(85,85,85)">]</span></a><br>
</p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>2D articulated human pose estimation software[<a href="http://groups.inf.ed.ac.uk/calvin/articulated_human_pose_estimation_code/">Project</a>]<br>
</p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Learning and detecting shape models [<a href="http://groups.inf.ed.ac.uk/calvin/release-learn-shapes-v1.3.tgz">code</a>]<br>
</p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Progressive Search Space Reduction for Human Pose Estimation[<a href="http://www.robots.ox.ac.uk/~vgg/software/UpperBody/index.html">Project</a>]<br>
</p>
<p align="left" style="background:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Learning Non-Rigid 3D Shape from 2D Motion[<a href="http://movement.stanford.edu/learning-nr-shape/">Project</a>]<br>
</p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">十二、图像处理：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#555555">Distance Transforms of Sampled Functions[<a href="http://cs.brown.edu/~pff/dt/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;
</span>The Computer Vision Homepage[<a href="http://www.cs.cmu.edu/~cil/vision.html">Project</a>]<br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;
</span><span style="color:rgb(85,85,85)">Efficient appearance distances between windows[<a href="http://groups.inf.ed.ac.uk/calvin/efficientAppDistances/releaseEfficientAppDistances.zip">code</a>]</span><br>
</span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Image Exploration algorithm[<a href="http://groups.inf.ed.ac.uk/calvin/ReleasedCode/image_exploration_v1.1.tgz">code</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Motion Magnification 运动放大 [<a href="http://people.csail.mit.edu/celiu/motionmag/motionmag.html">Project</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Bilateral Filtering for Gray and Color Images 双边滤波器 [<a href="http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html">Project</a>]<br>
</span></span></p>
<p align="left" style="background:white"><span style="color:#555555"><span style="color:rgb(85,85,85)"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>A Fast Approximation of the Bilateral Filter using a Signal Processing Approach [<a href="http://people.csail.mit.edu/sparis/bf/">Project]</a><br>
</span></span></p>
<p align="left" style="background:white"><strong><span style="font-size:14px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></p>
<p align="left" style="background:white"><strong><span style="font-size:18px">十三、一些实用工具：</span></strong></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">EGT: a Toolbox for Multiple View Geometry and Visual Servoing[<a href="http://egt.dii.unisi.it/"><span style="color:#0000ff">Project</span></a>] [<a href="http://egt.dii.unisi.it/download/EGT_v1p3.zip"><span style="color:#2970a6">Code</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">a development kit of matlab mex functions for OpenCV library[<a href="http://www.cs.stonybrook.edu/~kyamagu/mexopencv/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style="color:#555555">Fast Artificial Neural Network Library[<a href="http://leenissen.dk/fann/wp/"><span style="color:#0000ff">Project</span></a>]</span></p>
<p align="left" style="background:white"><span style="color:#555555">&nbsp;</span></p>
<p><span style="font-size:14px"><span style="color:#ff0000">&nbsp;</span></span></p>
<p align="left" style="background-color:white"><strong><span style="font-size:18px">十四、人手及指尖检测与识别：</span></strong></p>
<p align="left" style="color:red; background-color:white"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">finger-detection-and-gesture-recognition&nbsp;[<a href="http://code.google.com/p/finger-detection-and-gesture-recognition/downloads/list"><span style="color:rgb(41,112,166)">Code</span></a>]</span></p>
<p align="left" style="color:red; background-color:white"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Hand and Finger Detection using JavaCV[<a href="http://www.javacodegeeks.com/2012/12/hand-and-finger-detection-using-javacv.html?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+JavaCodeGeeks+%28Java+Code+Geeks%29"><span style="color:rgb(0,0,255)">Project</span></a>]</span></p>
<p align="left" style="color:red; background-color:white"><span style="color:rgb(85,85,85)">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:rgb(85,85,85)">Hand and fingers detection[<a href="http://forum.openframeworks.cc/index.php?topic=1916.0"><span style="color:rgb(0,0,255)">Code</span></a>]</span></p>
<p align="left" style="color:red; background-color:white"><span style="color:rgb(85,85,85)"><br>
</span></p>
<p align="left" style="background-color:white"></p>
<p align="left" style="font-size:14px; background-color:white"><strong><span style="font-size:18px">十五、场景解释：</span></strong></p>
<p align="left" style="font-size:14px; background-color:white">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nonparametric Scene Parsing via Label Transfer&nbsp;[<a href="http://people.csail.mit.edu/celiu/LabelTransfer/code.html">Project</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><br>
</p>
<p align="left" style="font-size:14px; background-color:white"></p>
<p align="left" style="font-size:14px; background-color:white"><strong><span style="font-size:18px">十六、光流Optical flow：</span></strong></p>
<p align="left" style="font-size:14px; background-color:white">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;High accuracy optical flow using a theory for warping&nbsp;[<a href="http://perception.inrialpes.fr/~chari/myweb/Software/">Project</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="font-size:14px">Dense Trajectories Video Description</span><span style="font-size:14px">&nbsp;[</span><a href="http://lear.inrialpes.fr/people/wang/dense_trajectories" style="font-size:14px">Project</a><span style="font-size:14px">]</span><br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>SIFT Flow: Dense Correspondence across Scenes and its Applications[<a href="http://people.csail.mit.edu/celiu/SIFTflow/">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>KLT: An Implementation of the Kanade-Lucas-Tomasi Feature Tracker [<a href="http://www.ces.clemson.edu/~stb/klt/">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Tracking Cars Using Optical Flow[<a href="http://www.mathworks.cn/cn/help/vision/examples/tracking-cars-using-optical-flow.html">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Secrets of optical flow estimation and their principles[<a href="http://ps.is.tue.mpg.de/person/black#tabs-code">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>implmentation of the Black and Anandan dense optical flow method<span style="font-size:14px">[</span><a href="http://ps.is.tue.mpg.de/person/black#tabs-code" style="font-size:14px">Project</a><span style="font-size:14px">]</span><br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Optical Flow Computation[<a href="https://www.ceremade.dauphine.fr/~peyre/numerical-tour/tours/multidim_5_opticalflow/#37">Project</a>]<br>
</span></p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Beyond Pixels: Exploring New Representations and Applications for Motion Analysis[<a href="http://people.csail.mit.edu/celiu/OpticalFlow/">Project</a>]<br>
</span></p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>A Database and Evaluation Methodology for Optical Flow[<a href="http://vision.middlebury.edu/flow/">Project</a>]<br>
</span></p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>optical flow relative[<a href="http://lmb.informatik.uni-freiburg.de/resources/software.php">Project</a>]</span></p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Robust Optical Flow Estimation [<a href="http://www.ipol.im/pub/pre/21/">Project</a>]<br>
</span></p>
<p align="left" style="font-size:14px; background-color:white"><span style="font-size:14px"><span style="font-size:14px"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>optical flow[</span><a href="http://www.jonathanmugan.com/GraphicsProject/OpticalFlow/" style="font-size:14px">Project</a><span style="font-size:14px">]</span><br>
</span></p>
<br>
<p align="left" style="font-size:14px; background-color:white"><strong><span style="font-size:18px">十七、图像检索<span style="font-size:18px"><strong>Image Retrieval</strong></span>：</span></strong></p>
<p align="left" style="font-size:14px; background-color:white">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Semi-Supervised Distance Metric Learning for Collaborative Image Retrieval&nbsp;<a href="http://www.ee.columbia.edu/~wliu/CVPR08_ssml.pdf">[Paper</a>][<a href="http://www.ee.columbia.edu/~wliu/SSMetric.zip">code</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><br>
</p>
<p align="left" style="font-size:14px; background-color:white"></p>
<p align="left" style="font-size:14px; background-color:white"><strong><span style="font-size:18px">十八、马尔科夫随机场Markov Random Fields：</span></strong></p>
<p align="left" style="font-size:14px; background-color:white">· &nbsp; &nbsp; &nbsp; &nbsp; Markov Random Fields for Super-Resolution&nbsp;<a href="http://www.ee.columbia.edu/~wliu/CVPR08_ssml.pdf">[</a><a href="http://people.csail.mit.edu/billf/project%20pages/sresCode/Markov%20Random%20Fields%20for%20Super-Resolution.html">Project</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>A Comparative Study of Energy Minimization Methods for Markov Random Fields with Smoothness-Based Priors [<a href="http://vision.middlebury.edu/MRF/">Project</a>]<br>
</p>
<br>
<p align="left" style="font-size:14px; background-color:white"><strong><span style="font-size:18px">十九、运动检测Motion detection：</span></strong></p>
<p align="left" style="font-size:14px; background-color:white">·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moving Object Extraction, Using Models or Analysis of Regions&nbsp;<a href="http://www.ee.columbia.edu/~wliu/CVPR08_ssml.pdf">[</a><a href="http://www.visionbib.com/bibliography/motion-i763.html">Project</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Background Subtraction: Experiments and Improvements for ViBe [<a href="http://www2.ulg.ac.be/telecom/publi/publications/mvd/VanDroogenbroeck2012Background/index.html">Project</a>]</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>A Self-Organizing Approach to Background Subtraction for Visual Surveillance Applications [<a href="http://www.na.icar.cnr.it/~maddalena.l/MODLab/SoftwareSOBS.html">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>changedetection.net: A new change detection benchmark dataset[<a href="http://www.changedetection.net/">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>ViBe - a powerful technique for background detection and subtraction in video sequences[<a href="http://www2.ulg.ac.be/telecom/research/vibe/">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Background Subtraction Program[<a href="http://www.umiacs.umd.edu/~knkim/UMD-BGS/index.html">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Motion Detection Algorithms[<a href="http://www.codeproject.com/Articles/10248/Motion-Detection-Algorithms">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Stuttgart Artificial Background Subtraction Dataset[<a href="http://www.vis.uni-stuttgart.de/index.php?id=sabs">Project</a>]<br>
</p>
<p align="left" style="font-size:14px; background-color:white"><span style="color:rgb(85,85,85)">· &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>Object Detection, Motion Estimation, and Tracking[<a href="http://www.mathworks.cn/cn/help/vision/motion-analysis-and-tracking.html">Project</a>]<br>
</p>
<br>
</div>
