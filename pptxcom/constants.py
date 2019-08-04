# -*- coding: utf-8 -*-
"""
Created on Sun Aug 4 15:33:33 2019
@author: Nathan Jones
"""

from enum import Enum, unique

@unique
class MsoAnimAccumulate(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimAccumulateNone = 1  # Does not accumulate.
	msoAnimAccumulateAlways = 2  # Accumulates with other animation behaviors.

@unique
class MsoAnimAdditive(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimAdditiveAddBase = 1  # Uses the animation behavior of the base animations.
	msoAnimAdditiveAddSum = 2  # Adds together the animation behavior of multiple animations.


@unique
class MsoAnimAfterEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimAfterEffectMixed = -1  # Mixed
	msoAnimAfterEffectNone = 0  # Unchanged
	msoAnimAfterEffectDim = 1  # Dimmed
	msoAnimAfterEffectHide = 2  # Hidden
	msoAnimAfterEffectHideOnNextClick = 3  # Hidden on the next mouse click

	
@unique
class MsoAnimateByLevel(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimateChartAllAtOnce = 7  # Animate chart all at once
	msoAnimateChartByCategory = 8  # Animate chart by category
	msoAnimateChartByCategoryElements = 9  # Animate chart by category elements
	msoAnimateChartBySeries = 10  # Animate chart by series
	msoAnimateChartBySeriesElements = 11  # Animate chart by series elements
	msoAnimateDiagramAllAtOnce = 12  # Animate diagram all at once
	msoAnimateDiagramBreadthByLevel = 16  # Animate diagram breadth by level
	msoAnimateDiagramBreadthByNode = 15  # Animate diagram breadth by node
	msoAnimateDiagramClockwise = 17  # Animate diagram clockwise
	msoAnimateDiagramClockwiseIn = 18  # Animate diagram clockwise in
	msoAnimateDiagramClockwiseOut = 19  # Animate diagram clockwise out
	msoAnimateDiagramCounterClockwise = 20  # Animate diagram counter-clockwise
	msoAnimateDiagramCounterClockwiseIn = 21  # Animate diagram counter-clockwise in
	msoAnimateDiagramCounterClockwiseOut = 22  # Animate diagram counter-clockwise out
	msoAnimateDiagramDepthByBranch = 14  # Animate diagram depth by branch
	msoAnimateDiagramDepthByNode = 13  # Animate diagram depth by node
	msoAnimateDiagramDown = 26  # Animate diagram down
	msoAnimateDiagramInByRing = 23  # Animate diagram in by ring
	msoAnimateDiagramOutByRing = 24  # Animate diagram out by ring
	msoAnimateDiagramUp = 25  # Animate diagram up
	msoAnimateLevelMixed = -1  # Animate level mixed
	msoAnimateLevelNone = 0  # Animate level none
	msoAnimateTextByAllLevels = 1  # Animate text by all levels
	msoAnimateTextByFifthLevel = 6  # Animate text by fifth level
	msoAnimateTextByFirstLevel = 2  # Animate text by first level
	msoAnimateTextByFourthLevel = 5  # Animate text by fourth level
	msoAnimateTextBySecondLevel = 3  # Animate text by second level
	msoAnimateTextByThirdLevel = 4  # Animate text by third level


@unique
class MsoAnimCommandType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimCommandTypeEvent = 0  # Event
	msoAnimCommandTypeCall = 1  # Call
	msoAnimCommandTypeVerb = 2  # Verb


@unique
class MsoAnimDirection(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimDirectionAcross = 18  # Across
	msoAnimDirectionBottom = 11  # Bottom
	msoAnimDirectionBottomLeft = 15  # Bottom Left
	msoAnimDirectionBottomRight = 14  # Bottom Right
	msoAnimDirectionCenter = 28  # Center
	msoAnimDirectionClockwise = 21  # Clockwise
	msoAnimDirectionCounterclockwise = 22  # Counterclockwise
	msoAnimDirectionCycleClockwise = 43  # Cycle Clockwise
	msoAnimDirectionCycleCounterclockwise = 44  # Cycle Counterclockwise
	msoAnimDirectionDown = 3  # Down
	msoAnimDirectionDownLeft = 9  # Down Left
	msoAnimDirectionDownRight = 8  # Down Right
	msoAnimDirectionFontAllCaps = 40  # Text is all caps
	msoAnimDirectionFontBold = 35  # Bold style is used
	msoAnimDirectionFontItalic = 36  # Italic style is used
	msoAnimDirectionFontShadow = 39  # Shadow style is used
	msoAnimDirectionFontStrikethrough = 38  # Strikethrough style is used
	msoAnimDirectionFontUnderline = 37  # Underlined style is used
	msoAnimDirectionGradual = 42  # Gradual
	msoAnimDirectionHorizontal = 16  # Horizontal
	msoAnimDirectionHorizontalIn = 23  # Horizontal In
	msoAnimDirectionHorizontalOut = 24  # Horizontal Out
	msoAnimDirectionIn = 19  # In
	msoAnimDirectionInBottom = 31  # In Bottom
	msoAnimDirectionInCenter = 30  # In Center
	msoAnimDirectionInSlightly = 29  # In Slightly
	msoAnimDirectionInstant = 41  # Appears Instantly
	msoAnimDirectionLeft = 4  # Appears from Left
	msoAnimDirectionNone = 0  # None
	msoAnimDirectionOrdinalMask = 5  # Ordinal Mask
	msoAnimDirectionOut = 20  # Out
	msoAnimDirectionOutBottom = 34  # Moves out from the Bottom
	msoAnimDirectionOutCenter = 33  # Moves out from the Center
	msoAnimDirectionOutSlightly = 32  # Slightly Out
	msoAnimDirectionRight = 2  # Moves to the Right
	msoAnimDirectionSlightly = 27  # Slightly
	msoAnimDirectionTop = 10  # Moves to the Top
	msoAnimDirectionTopLeft = 12  # Moves to the Top Left
	msoAnimDirectionTopRight = 13  # Moves to the Top Right
	msoAnimDirectionUp = 1  # Moves Up
	msoAnimDirectionUpLeft = 6  # Moves up to the Left
	msoAnimDirectionUpRight = 7  # Moves up to the Right
	msoAnimDirectionVertical = 17  # Moves Vertically
	msoAnimDirectionVerticalIn = 25  # Moves Vertically In
	msoAnimDirectionVerticalOut = 26  # Moves Vertically Out


@unique
class MsoAnimEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimEffectCustom = 0  # Custom Effect
	msoAnimEffectAppear = 1  # Appears
	msoAnimEffectFly = 2  # Fly Effect
	msoAnimEffectBlinds = 3  # Blinds
	msoAnimEffectBox = 4  # Box
	msoAnimEffectCheckerboard = 5  # Checkerboard Effect
	msoAnimEffectCircle = 6  # Circle
	msoAnimEffectCrawl = 7  # Crawl Effect
	msoAnimEffectDiamond = 8  # Diamond Effect
	msoAnimEffectDissolve = 9  # Dissolve Effect
	msoAnimEffectFade = 10  # Fade Effect
	msoAnimEffectFlashOnce = 11  # Flash Once
	msoAnimEffectPeek = 12  # Peek effect
	msoAnimEffectPlus = 13  # Plus effect
	msoAnimEffectRandomBars = 14  # Random Bars effect
	msoAnimEffectSpiral = 15  # Spiral effect
	msoAnimEffectSplit = 16  # Split effect
	msoAnimEffectStretch = 17  # Stretch effect
	msoAnimEffectStrips = 18  # Strips effect
	msoAnimEffectSwivel = 19  # Swivel effect
	msoAnimEffectWedge = 20  # Wedge effect
	msoAnimEffectWheel = 21  # Wheel effect
	msoAnimEffectWipe = 22  # Wipe effect
	msoAnimEffectZoom = 23  # Zoom effect
	msoAnimEffectRandomEffects = 24  # Random effects
	msoAnimEffectBoomerang = 25  # Boomerangs
	msoAnimEffectBounce = 26  # Bounce
	msoAnimEffectColorReveal = 27  # Color Revealed
	msoAnimEffectCredits = 28  # Credits Effect
	msoAnimEffectEaseIn = 29  # EaseIn Effect
	msoAnimEffectFloat = 30  # Float Effect
	msoAnimEffectGrowAndTurn = 31  # Grow and Turn Effect
	msoAnimEffectLightSpeed = 32  # Light Speed Effect
	msoAnimEffectPinwheel = 33  # Pinwel effect
	msoAnimEffectRiseUp = 34  # Rise Up effect
	msoAnimEffectSwish = 35  # Swish effect
	msoAnimEffectThinLine = 36  # Thin line effect
	msoAnimEffectUnfold = 37  # Unfold effect
	msoAnimEffectWhip = 38  # Whip effect
	msoAnimEffectAscend = 39  # Ascends
	msoAnimEffectCenterRevolve = 40  # Center Revolves
	msoAnimEffectFadedSwivel = 41  # Faded Swivel Effect
	msoAnimEffectDescend = 42  # Descend Effect
	msoAnimEffectSling = 43  # Sling effect
	msoAnimEffectSpinner = 44  # Spinner effect
	msoAnimEffectStretchy = 45  # Stretchy effect
	msoAnimEffectZip = 46  # Zip effect
	msoAnimEffectArcUp = 47  # Arcs Up
	msoAnimEffectFadedZoom = 48  # Faded Zoom Effect
	msoAnimEffectGlide = 49  # Glide Effect
	msoAnimEffectExpand = 50  # Expand Effect
	msoAnimEffectFlip = 51  # Flip Effect
	msoAnimEffectShimmer = 52  # Shimmer effect
	msoAnimEffectFold = 53  # Fold Effect
	msoAnimEffectChangeFillColor = 54  # FillColor Changes
	msoAnimEffectChangeFont = 55  # Font Changes
	msoAnimEffectChangeFontColor = 56  # Font Color Changes
	msoAnimEffectChangeFontSize = 57  # Font Size Changes
	msoAnimEffectChangeFontStyle = 58  # Font Style Changes
	msoAnimEffectGrowShrink = 59  # Grow and Shrink Effect
	msoAnimEffectChangeLineColor = 60  # Line color Changes
	msoAnimEffectSpin = 61  # Spin effect
	msoAnimEffectTransparency = 62  # Transparency effect
	msoAnimEffectBoldFlash = 63  # Bold Flash
	msoAnimEffectBlast = 64  # Blasts
	msoAnimEffectBoldReveal = 65  # Bold Reveals
	msoAnimEffectBrushOnColor = 66  # Brush on Color
	msoAnimEffectBrushOnUnderline = 67  # Brush on Underline
	msoAnimEffectColorBlend = 68  # Color Bleeds
	msoAnimEffectColorWave = 69  # Color Wave
	msoAnimEffectComplementaryColor = 70  # Complementary Color
	msoAnimEffectComplementaryColor2 = 71  # Complementary Color2
	msoAnimEffectContrastingColor = 72  # Contrasting Color
	msoAnimEffectDarken = 73  # Darken Effect
	msoAnimEffectDesaturate = 74  # Desaturate Effect
	msoAnimEffectFlashBulb = 75  # Flash Bulb Effect
	msoAnimEffectFlicker = 76  # Flicker Effect
	msoAnimEffectGrowWithColor = 77  # Grow with Color Effect
	msoAnimEffectLighten = 78  # Lighten Effect
	msoAnimEffectStyleEmphasis = 79  # Emphasis effect
	msoAnimEffectTeeter = 80  # Teeter effect
	msoAnimEffectVerticalGrow = 81  # Vertical Grow effect
	msoAnimEffectWave = 82  # Wave effect
	msoAnimEffectMediaPlay = 83  # Media Play Effect
	msoAnimEffectMediaPause = 84  # Media Pause Effect
	msoAnimEffectMediaStop = 85  # Media Stop Effect
	msoAnimEffectPathCircle = 86  # Moves on a Circular Path
	msoAnimEffectPathRightTriangle = 87  # Moves on a RightTriangle path
	msoAnimEffectPathDiamond = 88  # Moves on a Diamond path
	msoAnimEffectPathHexagon = 89  # Moves on a Hexagon path
	msoAnimEffectPath5PointStar = 90  # Path5PointStar Effect
	msoAnimEffectPathCrescentMoon = 91  # Moves on a Crescent Moon path
	msoAnimEffectPathSquare = 92  # Moves on a Square path
	msoAnimEffectPathTrapezoid = 93  # Moves on a Trapezoid path
	msoAnimEffectPathHeart = 94  # Moves on a Heart shape path
	msoAnimEffectPathOctagon = 95  # Moves on a Octagon path
	msoAnimEffectPath6PointStar = 96  # Path6PointStar Effect
	msoAnimEffectPathFootball = 97  # Moves on a Football path
	msoAnimEffectPathEqualTriangle = 98  # Moves on a equilateral triangle path
	msoAnimEffectPathParallelogram = 99  # Moves on a Parallelogram path
	msoAnimEffectPathPentagon = 100  # Moves on a Pentagon path
	msoAnimEffectPath4PointStar = 101  # Path4PointStar Effect
	msoAnimEffectPath8PointStar = 102  # Path8PointStar Effect
	msoAnimEffectPathTeardrop = 103  # Moves on a Teardrop path
	msoAnimEffectPathPointyStar = 104  # Moves on a PointyStar path
	msoAnimEffectPathCurvedSquare = 105  # Moves on a CurvedSquare path
	msoAnimEffectPathCurvedX = 106  # Moves on a Curved X path
	msoAnimEffectPathVerticalFigure8 = 107  # Moves on a VerticalFigure8 path
	msoAnimEffectPathCurvyStar = 108  # Moves on a Curvy Star path
	msoAnimEffectPathLoopdeLoop = 109  # Moves on a LoopdeLoop path
	msoAnimEffectPathBuzzsaw = 110  # Moves on the Buzzsaw path
	msoAnimEffectPathHorizontalFigure8 = 111  # Moves on a Horizontal Figure8 path
	msoAnimEffectPathPeanut = 112  # Moves on a Peanut path
	msoAnimEffectPathFigure8Four = 113  # Moves on a Figure8Four path
	msoAnimEffectPathNeutron = 114  # Moves on a Neutron path
	msoAnimEffectPathSwoosh = 115  # Moves on a Swoosh path
	msoAnimEffectPathBean = 116  # Moves on the Bean path
	msoAnimEffectPathPlus = 117  # Moves on a Plus path
	msoAnimEffectPathInvertedTriangle = 118  # Moves on a Inverted Triangle path
	msoAnimEffectPathInvertedSquare = 119  # Moves on a Inverted Square path
	msoAnimEffectPathLeft = 120  # Moves on a Left path
	msoAnimEffectPathTurnRight = 121  # Moves on a TurnRight path
	msoAnimEffectPathArcDown = 122  # Moves on the Arc Down path
	msoAnimEffectPathZigzag = 123  # Moves on a Zigzag path
	msoAnimEffectPathSCurve2 = 124  # Moves on a SCurve2 path
	msoAnimEffectPathSineWave = 125  # Moves on a SineWave path
	msoAnimEffectPathBounceLeft = 126  # Moves on the Bounce Left path
	msoAnimEffectPathDown = 127  # Moves on a Down path
	msoAnimEffectPathTurnUp = 128  # Moves on a TurnUp path
	msoAnimEffectPathArcUp = 129  # Moves on the Arc Up path
	msoAnimEffectPathHeartbeat = 130  # Moves on a Heart Beat path
	msoAnimEffectPathSpiralRight = 131  # Moves on a SpiralRight path
	msoAnimEffectPathWave = 132  # Moves on a Wave path
	msoAnimEffectPathCurvyLeft = 133  # Moves on a Curvy Left path
	msoAnimEffectPathDiagonalDownRight = 134  # Moves on a Diagonal Down-Right path
	msoAnimEffectPathTurnDown = 135  # Moves on a TurnDown path
	msoAnimEffectPathArcLeft = 136  # Moves on the Arc Left path
	msoAnimEffectPathFunnel = 137  # Moves on a Funnel path
	msoAnimEffectPathSpring = 138  # Moves on a Spring path
	msoAnimEffectPathBounceRight = 139  # Moves on the Bounce Right path
	msoAnimEffectPathSpiralLeft = 140  # Moves on a SpiralLeft path
	msoAnimEffectPathDiagonalUpRight = 141  # Moves on a Diagonal Up-Right path
	msoAnimEffectPathTurnUpRight = 142  # Moves on a TurnUpRight path
	msoAnimEffectPathArcRight = 143  # Moves on the Arc Right Path
	msoAnimEffectPathSCurve1 = 144  # Moves on a SCurve1 path
	msoAnimEffectPathDecayingWave = 145  # Moves on a Decaying Wave path
	msoAnimEffectPathCurvyRight = 146  # Moves on a Curvy Right path
	msoAnimEffectPathStairsDown = 147  # Moves on a StairsDown path
	msoAnimEffectPathUp = 148  # Moves on an Up path
	msoAnimEffectPathRight = 149  # Moves on a Right path


@unique
class MsoAnimEffectAfter(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimEffectAfterFreeze = 1  # After freeze.
	msoAnimEffectAfterRemove = 2  # After remove.
	msoAnimEffectAfterHold = 3  # After hold.
	msoAnimEffectAfterTransition = 4  # After transition.


@unique
class MsoAnimEffectRestart(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimEffectRestartAlways = 1  # Always restarts.
	msoAnimEffectRestartWhenOff = 2  # Restarts when animation is off.
	msoAnimEffectRestartNever = 3  # Never restarts.


@unique
class MsoAnimFilterEffectSubtype(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimFilterEffectSubtypeAcross = 9  # Across
	msoAnimFilterEffectSubtypeDown = 25  # Down
	msoAnimFilterEffectSubtypeDownLeft = 14  # Left
	msoAnimFilterEffectSubtypeDownRight = 16  # Right
	msoAnimFilterEffectSubtypeFromBottom = 13  # From Bottom
	msoAnimFilterEffectSubtypeFromLeft = 10  # From Left
	msoAnimFilterEffectSubtypeFromRight = 11  # From Right
	msoAnimFilterEffectSubtypeFromTop = 12  # From Top
	msoAnimFilterEffectSubtypeHorizontal = 5  # Horizontal
	msoAnimFilterEffectSubtypeIn = 7  # In
	msoAnimFilterEffectSubtypeInHorizontal = 3  # In Horizontal
	msoAnimFilterEffectSubtypeInVertical = 1  # In Vertical
	msoAnimFilterEffectSubtypeLeft = 23  # Left
	msoAnimFilterEffectSubtypeNone = 0  # None
	msoAnimFilterEffectSubtypeOut = 8  # Out
	msoAnimFilterEffectSubtypeOutHorizontal = 4  # Out Horizontal
	msoAnimFilterEffectSubtypeOutVertical = 2  # Out Vertical
	msoAnimFilterEffectSubtypeRight = 24  # Right
	msoAnimFilterEffectSubtypeSpokes1 = 18  # Spokes 1
	msoAnimFilterEffectSubtypeSpokes2 = 19  # Spokes 2
	msoAnimFilterEffectSubtypeSpokes3 = 20  # Spokes 3
	msoAnimFilterEffectSubtypeSpokes4 = 21  # Spokes 4
	msoAnimFilterEffectSubtypeSpokes8 = 22  # Spokes 8
	msoAnimFilterEffectSubtypeUp = 26  # Up
	msoAnimFilterEffectSubtypeUpLeft = 15  # Up Left
	msoAnimFilterEffectSubtypeUpRight = 17  # Up Right
	msoAnimFilterEffectSubtypeVertical = 6  # Vertical


@unique
class MsoAnimFilterEffectType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimFilterEffectTypeBarn = 1  # Barn
	msoAnimFilterEffectTypeBlinds = 2  # Blinds
	msoAnimFilterEffectTypeBox = 3  # Box
	msoAnimFilterEffectTypeCheckerboard = 4  # Checkerboard
	msoAnimFilterEffectTypeCircle = 5  # Circle
	msoAnimFilterEffectTypeDiamond = 6  # Diamond
	msoAnimFilterEffectTypeDissolve = 7  # Dissolve
	msoAnimFilterEffectTypeFade = 8  # Fade
	msoAnimFilterEffectTypeImage = 9  # Image
	msoAnimFilterEffectTypeNone = 0  # No effect
	msoAnimFilterEffectTypePixelate = 10  # Pixelate
	msoAnimFilterEffectTypePlus = 11  # Plus
	msoAnimFilterEffectTypeRandomBar = 12  # Random bars
	msoAnimFilterEffectTypeSlide = 13  # Slide
	msoAnimFilterEffectTypeStretch = 14  # Stretch
	msoAnimFilterEffectTypeStrips = 15  # Strips
	msoAnimFilterEffectTypeWedge = 16  # Wedge
	msoAnimFilterEffectTypeWheel = 17  # Wheel
	msoAnimFilterEffectTypeWipe = 18  # Wipe


@unique
class MsoAnimProperty(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimColor = 7  # Color
	msoAnimHeight = 4  # Height
	msoAnimNone = 0  # None
	msoAnimOpacity = 5  # Opacity
	msoAnimRotation = 6  # Rotation
	msoAnimShapeFillBackColor = 1007  # Shape filled with back color
	msoAnimShapeFillColor = 1005  # Shape filled with color
	msoAnimShapeFillOn = 1004  # Shape fill on
	msoAnimShapeFillOpacity = 1006  # Shape fill opacity
	msoAnimShapeLineColor = 1009  # Colored line
	msoAnimShapeLineOn = 1008  # Shape line on
	msoAnimShapePictureBrightness = 1001  # Brightness of the picture
	msoAnimShapePictureContrast = 1000  # Contrast of the picture
	msoAnimShapePictureGamma = 1002  # Gamma properties of the picture
	msoAnimShapePictureGrayscale = 1003  # Grayscale properties of the picture
	msoAnimShapeShadowColor = 1012  # Shadow properties of the picture
	msoAnimShapeShadowOffsetX = 1014  # Shadow Offset X
	msoAnimShapeShadowOffsetY = 1015  # ShadowOffset Y
	msoAnimShapeShadowOn = 1010  # Shadow on
	msoAnimShapeShadowOpacity = 1013  # Opacity of the shape's shadow
	msoAnimShapeShadowType = 1011  # Type of shadow
	msoAnimTextBulletCharacter = 111  # Text bullet character
	msoAnimTextBulletColor = 114  # Text bullet color
	msoAnimTextBulletFontName = 112  # Text bullet fontname
	msoAnimTextBulletNumber = 113  # Text bullet number
	msoAnimTextBulletRelativeSize = 115  # Relative size of text bullet
	msoAnimTextBulletStyle = 116  # Text bullet style
	msoAnimTextBulletType = 117  # Text bullet type
	msoAnimTextFontBold = 100  # Text font bold
	msoAnimTextFontColor = 101  # Text font color
	msoAnimTextFontEmboss = 102  # Text font emboss
	msoAnimTextFontItalic = 103  # Text font italic
	msoAnimTextFontName = 104  # Text font name
	msoAnimTextFontShadow = 105  # Text font shadow
	msoAnimTextFontSize = 106  # Text font size
	msoAnimTextFontStrikeThrough = 110  # Text font strikethrough
	msoAnimTextFontSubscript = 107  # Text font subscript
	msoAnimTextFontSuperscript = 108  # Text font superscript
	msoAnimTextFontUnderline = 109  # Text font underline
	msoAnimVisibility = 8  # Visibility
	msoAnimWidth = 3  # Width
	msoAnimX = 1  # X coordinate
	msoAnimY = 2  # Y coordinate


@unique
class MsoAnimTextUnitEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimTextUnitEffectMixed = -1  # Mixed effect.
	msoAnimTextUnitEffectByParagraph = 0  # By paragraph.
	msoAnimTextUnitEffectByCharacter = 1  # By character.
	msoAnimTextUnitEffectByWord = 2  # By word.


@unique
class MsoAnimTriggerType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimTriggerAfterPrevious = 3  # After the Previous button is clicked.
	msoAnimTriggerMixed = -1  # Mixed actions.
	msoAnimTriggerNone = 0  # No action associated as the trigger.
	msoAnimTriggerOnPageClick = 1  # When a page is clicked.
	msoAnimTriggerOnShapeClick = 4  # When a shape is clicked.
	msoAnimTriggerWithPrevious = 2  # When the Previous button is clicked.


@unique
class MsoAnimType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoAnimTypeNone = 0  # None
	msoAnimTypeColor = 2  # Color
	msoAnimTypeCommand = 6  # Command
	msoAnimTypeFilter = 7  # Filter
	msoAnimTypeMixed = -2  # Mixed
	msoAnimTypeMotion = 1  # Motion
	msoAnimTypeProperty = 5  # Property
	msoAnimTypeRotation = 4  # Rotation
	msoAnimTypeScale = 3  # Scale
	msoAnimTypeSet = 8  # Set


@unique
class MsoClickState(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	msoClickStateAfterAllAnimations = -2  # After all animations.
	msoClickStateBeforeAutomaticAnimations = -1  # Before automatic animations.


@unique
class MsoShapeType(Enum):
	"""    
	@Enum: inherets methods from the Enum class
	
	This class represents the various shape types available in PowerPoint.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/office.msoshapetype
	"""
	
	msoShapeTypeMixed = -2  # ShapeTypeMixed (-2)
	msoAutoShape = 1  # AutoShape (1)
	msoCallout = 2  # Callout (2)
	msoChart = 3  # Chart (3)
	msoComment = 4  # Comment (4)
	msoFreeform = 5  # Freeform (5)
	msoGroup = 6  # Group (6)
	msoEmbeddedOLEObject = 7  # EmbeddedOLEObject (7)
	msoFormControl = 8  # FormControl (8)
	msoLine = 9  # Line (9)
	msoLinkedOLEObject = 10  # LinkedOLEObject (10)
	msoLinkedPicture = 11  # LinkedPicture (11)
	msoOLEControlObject = 12  # OLEControlObject (12)
	msoPicture = 13  # Picture (13)
	msoPlaceholder = 14  # Placeholder (14)
	msoTextEffect = 15  # TextEffect (15)
	msoMedia = 16  # Media (16)
	msoTextBox = 17  # TextBox (17)
	msoScriptAnchor = 18  # ScriptAnchor (18)
	msoTable = 19  # Table (19)
	msoCanvas = 20  # Canvas (20)
	msoDiagram = 21  # Diagram (21)
	msoInk = 22  # Ink (22)
	msoInkComment = 23  # InkComment (23)
	msoIgxGraphic = 24  # SmartArt graphic
	# There is no 25
	msoWebVideo = 26  # Web video
	msoContentApp = 27  # Content Office Add-in
	msoGraphic = 28  # Graphic
	msoLinkedGraphic = 29  # Linked graphic
	mso3DModel = 30  # 3D model
	msoLinked3DModel = 31  # Linked 3D model


@unique
class PpActionType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppActionEndShow = 6  # Slide show ends.
	ppActionFirstSlide = 3  # Returns to the first slide.
	ppActionHyperlink = 7  # Hyperlink.
	ppActionLastSlide = 4  # Moves to the last slide.
	ppActionLastSlideViewed = 5  # Moves to the last slide viewed.
	ppActionMixed = -2  # Performs a mixed action.
	ppActionNamedSlideShow = 10  # Runs the slideshow.
	ppActionNextSlide = 1  # Moves to the next slide.
	ppActionNone = 0  # No action is performed.
	ppActionOLEVerb = 11  # OLE Verb.
	ppActionPlay = 12  # Begins the slideshow.
	ppActionPreviousSlide = 2  # Moves to the previous slide.
	ppActionRunMacro = 8  # Runs a macro.
	ppActionRunProgram = 9  # Runs a program.


@unique
class PpAdvanceMode(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAdvanceModeMixed = -2  # Mixed mode.
	ppAdvanceOnClick = 1  # Only when clicked.
	ppAdvanceOnTime = 2  # Automatically after a specified amount of time.


@unique
class PpAfterEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAfterEffectDim = 2  # Appears dimmed
	ppAfterEffectHide = 1  # Hides
	ppAfterEffectHideOnClick = 3  # Hidden when clicked
	ppAfterEffectMixed = -2  # Mixed effect
	ppAfterEffectNothing = 0  # No effect


@unique
class PpAlertLevel(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAlertsNone = 1  # No alerts displayed.
	ppAlertsAll = 2  # All alerts displayed.


@unique
class PpArrangeStyle(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppArrangeTiled = 1  # Tiled
	ppArrangeCascade = 2  # Cascade


@unique
class PpAutoSize(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAutoSizeMixed = -2  # Mixed size.
	ppAutoSizeNone = 0  # Does not change size.
	ppAutoSizeShapeToFitText = 1  # Auto sizes the shape to fit the text.


@unique
class PpBaselineAlignment(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppBaselineAlignBaseline = 1  # Aligned to the baseline.
	ppBaselineAlignCenter = 3  # Aligned to the center.
	ppBaselineAlignFarEast50 = 4  # Align FarEast50.
	ppBaselineAlignMixed = -2  # Mixed alignment.
	ppBaselineAlignTop = 2  # Aligned to the top.


@unique
class PpBorderType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppBorderTop = 1  # Top    
	ppBorderLeft = 2  # Left
	ppBorderBottom = 3  # Bottom
	ppBorderRight = 4  # Right
	ppBorderDiagonalDown = 5  # Diagonally down
	ppBorderDiagonalUp = 6  # Diagonally up


@unique    
class PpBulletType(Enum):
	"""    
	@Enum: inherets methods from the Enum class
	
	Specifies the type of bullet.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppbullettype
	"""
	
	ppBulletMixed = -2  # Mixed bullets
	ppBulletNone = 0  # No bullets
	ppBulletUnnumbered = 1  # Unnumbered bullets
	ppBulletNumbered = 2  # Numbered bullets
	ppBulletPicture = 3  # Bullets with an image


@unique
class PpChangeCase(Enum):
	"""
	@Enum: inherets methods from the Enum class
	
	Specifies the way the case of the specified text will be changed.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppchangecase
	"""
	
	ppCaseSentence = 1  # Change to lowercase.
	ppCaseLower = 2  # Change to lowercase.
	ppCaseUpper = 3  # Change to uppercase.
	ppCaseTitle = 4  # Change to title case.
	ppCaseToggle = 5  # Toggle upper and lower casing.


@unique
class PpChartUnitEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAnimateByCategory = 2  # By category
	ppAnimateByCategoryElements = 4  # By category elements
	ppAnimateBySeries = 1  # By series
	ppAnimateBySeriesElements = 3  # By series elements
	ppAnimateChartAllAtOnce = 5  # Chart all at once
	ppAnimateChartMixed = -2  # Chart mixed


@unique
class PpCheckInVersionType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppCheckInMinorVersion = 0  # Minor version
	ppCheckInMajorVersion = 1  # Major version
	ppCheckInOverwriteVersion = 2  # Overwrite current version


@unique
class PpColorSchemeIndex(Enum):
	"""
	@Enum: inherets methods from the Enum class
	
	Specifies the color in the applied color scheme that is associated with the specified object.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppcolorschemeindex
	"""
	
	ppSchemeColorMixed = -2  # Mixed scheme color
	ppNotSchemeColor = 0  # Not scheme color
	ppBackground = 1  # Background
	ppForeground = 2  # Foreground
	ppShadow = 3  # Shadow
	ppTitle = 4  # Title
	ppFill = 5  # Fill
	ppAccent1 = 6  # Accent1
	ppAccent2 = 7  # Accent2
	ppAccent3 = 8  # Accent3


@unique
class PpDateTimeFormat(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppDateTimeddddMMMMddyyyy = 2  # ddddMMMMddyyyy
	ppDateTimedMMMMyyyy = 3  # dMMMMyyyy
	ppDateTimedMMMyy = 5  # dMMMyy
	ppDateTimeFigureOut = 14  # Figure Out
	ppDateTimeFormatMixed = -2  # Mixed Format
	ppDateTimeHmm = 10  # Hmm
	ppDateTimehmmAMPM = 12  # hmmAMPM
	ppDateTimeHmmss = 11  # Hmmss
	ppDateTimehmmssAMPM = 13  # hmmssAMPM
	ppDateTimeMdyy = 1  # Mdyy
	ppDateTimeMMddyyHmm = 8  # MMddyyHmm
	ppDateTimeMMddyyhmmAMPM = 9  # MMddyyhmmAMPM
	ppDateTimeMMMMdyyyy = 4  # MMMMdyyyy
	ppDateTimeMMMMyy = 6  # MMMMyy
	ppDateTimeMMyy = 7  # MMyy


@unique
class PpDirection(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppDirectionLeftToRight = 1  # Left-to-right layout
	ppDirectionMixed = -2  # Mixed layout
	ppDirectionRightToLeft = 2  # Right-to-left layout


@unique
class PpEntryEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppEffectNone = 0  # None
	ppEffectMixed = -2  # Mixed
	ppEffectAppear = 3844  # Appear
	ppEffectBlindsHorizontal = 769  # Blinds Horizontal
	ppEffectBlindsVertical = 770  # Blinds Vertical
	ppEffectBoxIn = 3074  # Box In
	ppEffectBoxOut = 3073  # Box Out
	ppEffectCheckerboardAcross = 1025  # Checkerboard Across
	ppEffectCheckerboardDown = 1026  # Checkerboard Down
	ppEffectCircleOut = 3845  # Circle Out
	ppEffectCombHorizontal = 3847  # Comb Horizontal
	ppEffectCombVertical = 3848  # Comb Vertical
	ppEffectCoverDown = 1284  # Cover Down
	ppEffectCoverLeft = 1281  # Cover Left
	ppEffectCoverLeftDown = 1287  # Cover Left Down
	ppEffectCoverLeftUp = 1285  # Cover Left Up
	ppEffectCoverRight = 1283  # 
	ppEffectCoverRightDown = 1288  # Cover Right Down
	ppEffectCoverRightUp = 1286  # Cover Right Up
	ppEffectCoverUp = 1282  # Cover Up
	ppEffectCrawlFromDown = 3344  # Crawl From Down
	ppEffectCrawlFromLeft = 3341  # Crawl From Left
	ppEffectCrawlFromRight = 3343  # Crawl From Right
	ppEffectCrawlFromUp = 3342  # Crawl From Up
	ppEffectCut = 257  # Cut
	ppEffectCutThroughBlack = 258  # Cut Through Black
	ppEffectDiamondOut = 3846  # Diamond Out
	ppEffectDissolve = 1537  # Dissolve
	ppEffectFade = 1793  # Fade
	ppEffectFadeSmoothly = 3849  # Fade Smoothly
	ppEffectFlashOnceFast = 3841  # Flash Once Fast
	ppEffectFlashOnceMedium = 3842  # Flash Once Medium
	ppEffectFlashOnceSlow = 3843  # Flash Once Slow
	ppEffectFlyFromBottom = 3332  # Fly From Bottom
	ppEffectFlyFromBottomLeft = 3335  # From Bottom Left
	ppEffectFlyFromBottomRight = 3336  # From Bottom Right
	ppEffectFlyFromLeft = 3329  # Fly From Left
	ppEffectFlyFromRight = 3331  # Fly From Right
	ppEffectFlyFromTop = 3330  # Fly From Top
	ppEffectFlyFromTopLeft = 3333  # Fly From Top Left
	ppEffectFlyFromTopRight = 3334  # Fly From Top Right
	ppEffectNewsflash = 3850  # Newsflash
	ppEffectPeekFromDown = 3338  # Peek From Down
	ppEffectPeekFromLeft = 3337  # Peek From Left
	ppEffectPeekFromRight = 3339  # Peek From Right
	ppEffectPeekFromUp = 3340  # Peek From Up
	ppEffectPlusOut = 3851  # Plus Out
	ppEffectPushDown = 3852  # Push Down
	ppEffectPushLeft = 3853  # Push Left
	ppEffectPushRight = 3854  # Push Right
	ppEffectPushUp = 3855  # Push Up
	ppEffectRandom = 513  # Random
	ppEffectRandomBarsHorizontal = 2305  # Random Bars Horizontal
	ppEffectRandomBarsVertical = 2306  # Random Bars Vertical
	ppEffectSpiral = 3357  # Spiral
	ppEffectSplitHorizontalIn = 3586  # Split Horizontal In
	ppEffectSplitHorizontalOut = 3585  # Split Horizontal Out
	ppEffectSplitVerticalIn = 3588  # Split Vertical In
	ppEffectSplitVerticalOut = 3587  # Split Vertical Out
	ppEffectStretchAcross = 3351  # Stretch Across
	ppEffectStretchDown = 3355  # Stretch Down
	ppEffectStretchLeft = 3352  # Stretch Left
	ppEffectStretchRight = 3354  # Stretch Right
	ppEffectStretchUp = 3353  # Stretch Up
	ppEffectStripsDownLeft = 2563  # Strips Down Left
	ppEffectStripsDownRight = 2564  # Strips Down Right
	ppEffectStripsLeftDown = 2567  # Strips Left Down
	ppEffectStripsLeftUp = 2565  # Strips Left Up
	ppEffectStripsRightDown = 2568  # Strips Right Down
	ppEffectStripsRightUp = 2566  # Strips Right Up
	ppEffectStripsUpLeft = 2561  # Strips Up Left
	ppEffectStripsUpRight = 2562  # Strips Up Right
	ppEffectSwivel = 3356  # Swivel
	ppEffectUncoverDown = 2052  # Uncover Down
	ppEffectUncoverLeft = 2049  # Uncover Left
	ppEffectUncoverLeftDown = 2055  # Uncover Left Down
	ppEffectUncoverLeftUp = 2053  # Uncover Left Up
	ppEffectUncoverRight = 2051  # Effect Uncover Right
	ppEffectUncoverRightDown = 2056  # Uncover Right Down
	ppEffectUncoverRightUp = 2054  # Uncover Right Up
	ppEffectUncoverUp = 2050  # Uncover Up
	ppEffectWedge = 3856  # Wedge
	ppEffectWheel1Spoke = 3857  # Wheel1 Spoke
	ppEffectWheel2Spokes = 3858  # Wheel2 Spokes
	ppEffectWheel3Spokes = 3859  # Wheel3 Spokes
	ppEffectWheel4Spokes = 3860  # Wheel4 Spokes
	ppEffectWheel8Spokes = 3861  # Wheel8 Spokes
	ppEffectWipeDown = 2820  # Wipe Down
	ppEffectWipeLeft = 2817  # Wipe Left
	ppEffectWipeRight = 2819  # Wipe Right
	ppEffectWipeUp = 2818  # Wipe Up
	ppEffectZoomBottom = 3350  # Zoom Bottom
	ppEffectZoomCenter = 3349  # Zoom Center
	ppEffectZoomIn = 3345  # Zoom In
	ppEffectZoomInSlightly = 3346  # Zoom In Slightly
	ppEffectZoomOut = 3347  # Zoom Out
	ppEffectZoomOutSlightly = 3348  # Zoom Out Slightly


@unique
class PpFarEastLineBreakLevel(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppFarEastLineBreakLevelNormal = 1  # Normal level
	ppFarEastLineBreakLevelStrict = 2  # Strict level
	ppFarEastLineBreakLevelCustom = 3  # Custom level
	

@unique
class PpFixedFormatIntent(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	pFixedFormatIntentPrint = 2  # Intent is to print exported file.
	ppFixedFormatIntentScreen = 1  # Intent is to view exported file on screen.


@unique
class PpFixedFormatType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppFixedFormatTypePDF = 2  # PDF format
	ppFixedFormatTypeXPS = 1  # XPS format


@unique
class PpFollowColors(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppFollowColorsMixed = -2  # The chart colors follow a mixed format of the slide's color scheme.
	ppFollowColorsNone = 0  # The chart colors do not follow the slide's color scheme.    
	ppFollowColorsScheme = 1  # All the colors in the chart follow the slide's color scheme.
	ppFollowColorsTextAndBackground = 2  ## Only the text and background follow the slide's color scheme.    



@unique
class PpGuideOrientation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppHorizontalGuide = 1  # Represents a horizontal guide, spanning from the left to right of the slide editing window.
	ppVerticalGuide = 2  # Represents a vertical guide, spanning from top edge to bottom of the slide editing window.


@unique
class PpHTMLVersion(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppHTMLv3 = 1  # HTML Version 3
	ppHTMLv4 = 2  # HTML Version 4 (Default)
	ppHTMLDual = 3  # Dual version
	ppHTMLAutodetect = 4  # Autodetect
	

@unique
class PpMediaTaskStatus(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppMediaTaskStatusNone = 0  # No status
	ppMediaTaskStatusInProgress = 1  # In progress
	ppMediaTaskStatusQueued = 2  # Queued
	ppMediaTaskStatusDone = 3  # Done
	ppMediaTaskStatusFailed = 4  # Failed


@unique
class PpMediaType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppMediaTypeMixed = -2  # Mixed
	ppMediaTypeOther = 1  # Others
	ppMediaTypeSound = 2  # Sound
	ppMediaTypeMovie = 3  # Movie


@unique
class PpMouseActivation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppMouseClick = 1  # Mouse click
	ppMouseOver = 2  # Mouse over


@unique
class PpNumberedBulletStyle(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppBulletAlphaLCParenBoth = 8  # Lowercase alphabetical characters with both parentheses.
	ppBulletAlphaLCParenRight = 9  # Lowercase alphabetical characters with closing parenthesis.
	ppBulletAlphaLCPeriod = 0  # Lowercase alphabetical characters with a period.
	ppBulletAlphaUCParenBoth = 10  # Uppercase alphabetical characters with both parentheses.
	ppBulletAlphaUCParenRight = 11  # Uppercase alphabetical characters with closing parenthesis.
	ppBulletAlphaUCPeriod = 1  # Uppercase alphabetical characters with a period.
	ppBulletArabicAbjadDash = 24  # Arabic Abjad alphabets with a dash.
	ppBulletArabicAlphaDash = 23  # Arabic language alphabetical characters with a dash.
	ppBulletArabicDBPeriod = 29  # Double-byte Arabic numbering scheme with double-byte period.
	ppBulletArabicDBPlain = 28  # Double-byte Arabic numbering scheme (no punctuation).
	ppBulletArabicParenBoth = 12  # Arabic numerals with both parentheses.
	ppBulletArabicParenRight = 2  # Arabic numerals with closing parenthesis.
	ppBulletArabicPeriod = 3  # Arabic numerals with a period.
	ppBulletArabicPlain = 13  # Arabic numerals.
	ppBulletCircleNumDBPlain = 18  # Double-byte circled number for values up to 10.
	ppBulletCircleNumWDBlackPlain = 20  # Shadow color number with circular background of normal text color.
	ppBulletCircleNumWDWhitePlain = 19  # Text colored number with same color circle drawn around it.
	ppBulletHebrewAlphaDash = 25  # Hebrew language alphabetical characters with a dash.
	ppBulletHindiAlpha1Period = 40  # Hindi Alpha1 period.
	ppBulletHindiAlphaPeriod = 36  # Hindi Alpha period.
	ppBulletHindiNumParenRight = 39  # Hindi Num Paren right.
	ppBulletHindiNumPeriod = 37  # Hindi Num period.
	ppBulletKanjiKoreanPeriod = 27  # Japanese/Korean numbers with a period.
	ppBulletKanjiKoreanPlain = 26  # Japanese/Korean numbers without a period.
	ppBulletKanjiSimpChinDBPeriod = 38  # Kanji Simple Chinese DBPeriod
	ppBulletRomanLCParenBoth = 4  # Lowercase Roman numerals with both parentheses.
	ppBulletRomanLCParenRight = 5  # Lowercase Roman numerals with closing parenthesis.
	ppBulletRomanLCPeriod = 6  # Lowercase Roman numerals with period.
	ppBulletRomanUCParenBoth = 14  # Uppercase Roman numerals with both parentheses.
	ppBulletRomanUCParenRight = 15  # Uppercase Roman numerals with closing parenthesis.
	ppBulletRomanUCPeriod = 7  # Uppercase Roman numerals with period.
	ppBulletSimpChinPeriod = 17  # Simplified Chinese with a period.
	ppBulletSimpChinPlain = 16  # Simplified Chinese without a period.
	ppBulletStyleMixed = -2  # Any undefined style.
	ppBulletThaiAlphaParenBoth = 32  # Thai Alpha Paren both.
	ppBulletThaiAlphaParenRight = 31  # Thai Alpha Paren right.
	ppBulletThaiAlphaPeriod = 30  # Thai Alpha period.
	ppBulletThaiNumParenBoth = 35  # Thai Num Paren both.
	ppBulletThaiNumParenRight = 34  # Thai Num Paren right.
	ppBulletThaiNumPeriod = 33  # Thai Num period.
	ppBulletTradChinPeriod = 22  # Traditional Chinese with a period.
	ppBulletTradChinPlain = 21  # Traditional Chinese without a period.


@unique
class PpParagraphAlignment(Enum):
	"""
	@Enum: inherets methods from the Enum class
	
	Specifies the alignment for each paragraph in the specified paragraph format.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppparagraphalignment    
	"""
	
	ppAlignmentMixed = -2  # Mixed alignment
	ppAlignLeft = 1  # Left aligned
	ppAlignCenter = 2  # Center align
	ppAlignRight = 3  # Right-aligned
	ppAlignJustify = 4  # Justify
	ppAlignDistribute = 5  # Distribute
	ppAlignThaiDistribute = 6  # Thai distributed
	ppAlignJustifyLow = 7  # Low justify


@unique
class PpPasteDataType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPasteBitmap = 1  # Paste bitmap.
	ppPasteDefault = 0  # Paste the default content of the clipboard.
	ppPasteEnhancedMetafile = 2  # Paste enhanced Metafile
	ppPasteGIF = 4  # Paste a GIF image.
	ppPasteHTML = 8  # Paste HTML.
	ppPasteJPG = 5  # Paste a JPG image.
	ppPasteMetafilePicture = 3  # Paste a Metafile picture.
	ppPasteOLEObject = 10  # Paste OLE object.
	ppPastePNG = 6  # Paste PNG image.
	ppPasteRTF = 9  # Paste RTF.
	ppPasteShape = 11  # Paste a shape.
	ppPasteText = 7  # Paste text.


@unique
class PpPlaceholderType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPlaceholderBitmap = 9  # Bitmap
	ppPlaceholderBody = 2  # Body
	ppPlaceholderCenterTitle = 3  # Center Title
	ppPlaceholderChart = 8  # Chart
	ppPlaceholderDate = 16  # Date
	ppPlaceholderFooter = 15  # Footer
	ppPlaceholderHeader = 14  # Header
	ppPlaceholderMediaClip = 10  # Media Clip
	ppPlaceholderMixed = -2  # Mixed
	ppPlaceholderObject = 7  # Object
	ppPlaceholderOrgChart = 11  # Organization Chart
	ppPlaceholderPicture = 18  # Picture
	ppPlaceholderSlideNumber = 13  # Slide Number
	ppPlaceholderSubtitle = 4  # Subtitle
	ppPlaceholderTable = 12  # Table
	ppPlaceholderTitle = 1  # Title
	ppPlaceholderVerticalBody = 6  # Vertical Body
	ppPlaceholderVerticalObject = 17  # Vertical Object
	ppPlaceholderVerticalTitle = 5  # Vertical Title


@unique
class PpPlayerState(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPlaying = 0  # Playing
	ppPaused = 1  # Paused
	ppStopped = 2  # Stopped
	ppNotReady = 3  # Not ready


@unique
class PpPrintColorType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPrintBlackAndWhite = 2  # Black and White
	ppPrintColor = 1  # Colored
	ppPrintPureBlackAndWhite = 3  # Pure Black and White


@unique
class PpPrintHandoutOrder(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPrintHandoutHorizontalFirst = 2  # Slides are ordered horizontally, with the first slide in the upper-left corner and the second slide to the right of it. If your language setting specifies a right-to-left language, the first slide is in the upper-right corner with the second slide to the left of it.
	ppPrintHandoutVerticalFirst = 1  # Slides are ordered vertically, with the first slide in the upper-left corner and the second slide below it. If your language setting specifies a right-to-left language, the first slide is in the upper-right corner with the second slide below it.


@unique
class PpPrintOutputType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPrintOutputBuildSlides = 7  # Build Slides
	ppPrintOutputFourSlideHandouts = 8  # Four Slide Handouts
	ppPrintOutputNineSlideHandouts = 9  # Nine Slide Handouts
	ppPrintOutputNotesPages = 5  # Notes Pages
	ppPrintOutputOneSlideHandouts = 10  # Single Slide Handouts
	ppPrintOutputOutline = 6  # Outline
	ppPrintOutputSixSlideHandouts = 4  # Six Slide Handouts
	ppPrintOutputSlides = 1  # Slides
	ppPrintOutputThreeSlideHandouts = 3  # Three Slide Handouts
	ppPrintOutputTwoSlideHandouts = 2  # Two Slide Handouts


@unique
class PpPrintRangeType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPrintAll = 1  # Print all slides in the presentation.
	ppPrintCurrent = 3  # Print the current slide from the presentation.
	ppPrintNamedSlideShow = 5  # Print a named slideshow.
	ppPrintSelection = 2  # Print a selection of slides.
	ppPrintSlideRange = 4  # Print a range of slides.


@unique
class PpProtectedViewCloseReason(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppProtectedViewCloseNormal = 0  # Protected view is being closed normally.
	ppProtectedViewCloseEdit = 1  # Protected view is being closed so that the presentation can be edited.
	ppProtectedViewCloseForced = 2  # Protected view is forced closed.


@unique
class PpPublishSourceType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppPublishAll = 1  # Publish all.
	ppPublishNamedSlideShow = 3  # Publish a named slideshow.
	ppPublishSlideRange = 2  # Publish a range of slides.


@unique
class PpRemoveDocInfoType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppRDIAll = 99  # Remove all document information.
	ppRDIAtMentions = 18  # Remove resolved @mentioned users from comments.
	ppRDIComments = 1  # Remove comments.
	ppRDIContentType = 16  # Remove content type information.
	ppRDIDocumentManagementPolicy = 15  # Remove document management policy information.
	ppRDIDocumentProperties = 8  # Remove document properties.
	ppRDIDocumentServerProperties = 14  # Remove document server properties.
	ppRDIDocumentWorkspace = 10  # Remove document workspace information.
	ppRDIInkAnnotations = 11  # Remove Ink annotations. NOTE(Enum): This constant has been deprecated, but it remains part of the object model for backward compatibility. You should not use it in new applications.
	ppRDIPublishPath = 13  # Remove publication path information.
	ppRDIRemovePersonalInformation = 4  # Remove personal information.
	ppRDISlideUpdateInformation = 17  # Remove slide update information.


@unique
class PpResampleMediaProfile(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppResampleMediaProfileCustom = 1  # Custom profile
	ppResampleMediaProfileSmall = 2  # Small profile
	ppResampleMediaProfileSmaller = 3  # Smaller profile
	ppResampleMediaProfileSmallest = 4  # Smallest profile


@unique
class PpRevisionInfo(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppRevisionInfoNone = 0  # No information.
	ppRevisionInfoBaseline = 1  # Information baseline.
	ppRevisionInfoMerged = 2  # Information merged.


@unique
class PpSaveAsFileType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSaveAsAddIn = 8  # 
	ppSaveAsBMP = 19  # 
	ppSaveAsDefault = 11  # 
	ppSaveAsEMF = 23  # 
	ppSaveAsExternalConverter = 64000  # 
	ppSaveAsGIF = 16  # 
	ppSaveAsJPG = 17  # 
	ppSaveAsMetaFile = 15  # 
	ppSaveAsMP4 = 39  # 
	ppSaveAsOpenDocumentPresentation = 35  # 
	ppSaveAsOpenXMLAddin = 30  # 
	ppSaveAsOpenXMLPicturePresentation = 36  # 
	ppSaveAsOpenXMLPresentation = 24  # 
	ppSaveAsOpenXMLPresentationMacroEnabled = 25  # 
	ppSaveAsOpenXMLShow = 28  # 
	ppSaveAsOpenXMLShowMacroEnabled = 29  # 
	ppSaveAsOpenXMLTemplate = 26  # 
	ppSaveAsOpenXMLTemplateMacroEnabled = 27  # 
	ppSaveAsOpenXMLTheme = 31  # 
	ppSaveAsPDF = 32  # 
	ppSaveAsPNG = 18  # 
	ppSaveAsPresentation = 1  # 
	ppSaveAsRTF = 6  # 
	ppSaveAsShow = 7  # 
	ppSaveAsStrictOpenXMLPresentation = 38  # 
	ppSaveAsTemplate = 5  # 
	ppSaveAsTIF = 21  # 
	ppSaveAsWMV = 37  # 
	ppSaveAsXMLPresentation = 34  # 
	ppSaveAsXPS = 33  # 


@unique
class PpSelectionType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	
	Constants that specify the type of selection, returned by the Type property of the Selection object.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppselectiontype
	"""
	
	ppSelectionNone = 0  # None
	ppSelectionSlides = 1  # Slides
	ppSelectionShapes = 2  # Shapes
	ppSelectionText = 3  # Text


@unique
class PpSlideLayout(Enum):
	"""
	@Enum: inherets methods from the Enum class
	
	Constants that specify the layout of the slide, passed to and returned by the Layout property of the Slide and SlideRange objects.
	
	https(Enum)://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppslidelayout
	"""
	
	ppLayoutMixed = -2  # Mixed
	ppLayoutTitle = 1  # Title
	ppLayoutText = 2  # Text
	ppLayoutTwoColumnText = 3  # Two-column text
	ppLayoutTable = 4  # Table
	ppLayoutTextAndChart = 5  # Text and chart
	ppLayoutChartAndText = 6  # Chart and text
	ppLayoutOrgchart = 7  # Organization chart
	ppLayoutChart = 8  # Chart
	ppLayoutTextAndClipArt = 9  # Text and ClipArt
	ppLayoutClipArtAndText = 10  # ClipArt and text
	ppLayoutTitleOnly = 11  # Title only
	ppLayoutBlank = 12  # Blank
	ppLayoutTextAndObject = 13  # Text and object
	ppLayoutObjectAndText = 14  # Object and text
	ppLayoutLargeObject = 15  # Large object
	ppLayoutObject = 16  # Object
	ppLayoutTextAndMediaClip = 17  # Text and MediaClip
	ppLayoutMediaClipAndText = 18  # MediaClip and text
	ppLayoutObjectOverText = 19  # Object over text
	ppLayoutTextOverObject = 20  # Text over object
	ppLayoutTextAndTwoObjects = 21  # Text and two objects
	ppLayoutTwoObjectsAndText = 22  # Two objects and text
	ppLayoutTwoObjectsOverText = 23  # Two objects over text
	ppLayoutFourObjects = 24  # Four objects
	ppLayoutVerticalText = 25  # Vertical text
	ppLayoutClipArtAndVerticalText = 26  # ClipArt and vertical text
	ppLayoutVerticalTitleAndText = 27  # Vertical title and text
	ppLayoutVerticalTitleAndTextOverChart = 28  # Vertical title and text over chart
	ppLayoutTwoObjects = 29  # Two objects
	ppLayoutObjectAndTwoObjects = 30  # Object and two objects
	ppLayoutTwoObjectsAndObject = 31  # Two objects and object
	ppLayoutCustom = 32  # Custom
	ppLayoutSectionHeader = 33  # Section header
	ppLayoutComparison = 34  # Comparison
	ppLayoutContentWithCaption = 35  # Content with caption
	ppLayoutPictureWithCaption = 36  # Picture with caption


@unique
class PpSlideShowAdvanceMode(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSlideShowManualAdvance = 1  # Manual Advance
	ppSlideShowUseSlideTimings = 2  # Specified timings for each slide
	ppSlideShowRehearseNewTimings = 3  # Rehearsed timings


@unique
class PpSlideShowPointerType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSlideShowPointerAlwaysHidden = 3  # Pointer is always hidden.
	ppSlideShowPointerArrow = 1  # Arrow pointer used.
	ppSlideShowPointerAutoArrow = 4  # AutoArrow pointer used.
	ppSlideShowPointerEraser = 5  # Eraser pointer used.
	ppSlideShowPointerNone = 0  # No pointer used.
	ppSlideShowPointerPen = 2  # Pen pointer used.


@unique
class PpSlideShowRangeType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppShowAll = 1  # Show all.
	ppShowNamedSlideShow = 3  # Show named slideshow.
	ppShowSlideRange = 2  # Show slide range.


@unique
class PpSlideShowState(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSlideShowBlackScreen = 3  # Black screen
	ppSlideShowDone = 5  # Done
	ppSlideShowPaused = 2  # Paused
	ppSlideShowRunning = 1  # Running
	ppSlideShowWhiteScreen = 4  # White screen


@unique
class PpSlideShowType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppShowTypeKiosk = 3  # Kiosk
	ppShowTypeSpeaker = 1  # Speaker
	ppShowTypeWindow = 2  # Window


@unique
class PpSlideSizeType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSlideSize35MM = 4  # 35MM
	ppSlideSizeA3Paper = 9  # A3 Paper
	ppSlideSizeA4Paper = 3  # A4 Paper
	ppSlideSizeB4ISOPaper = 10  # B4 ISO Paper
	ppSlideSizeB4JISPaper = 12  # B4 JIS Paper
	ppSlideSizeB5ISOPaper = 11  # B5 ISO Paper
	ppSlideSizeB5JISPaper = 13  # B5 JIS Paper
	ppSlideSizeBanner = 6  # Banner
	ppSlideSizeCustom = 7  # Custom
	ppSlideSizeHagakiCard = 14  # Hagaki Card
	ppSlideSizeLedgerPaper = 8  # Ledger Paper
	ppSlideSizeLetterPaper = 2  # Letter Paper
	ppSlideSizeOnScreen = 1  # On Screen
	ppSlideSizeOverhead = 5  # Overhead


@unique
class PpSoundEffectType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSoundEffectsMixed = -2  # Mixed
	ppSoundFile = 2  # File
	ppSoundNone = 0  # None
	ppSoundStopPrevious = 1  # Stop Previous


@unique
class PpSoundFormatType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppSoundFormatCDAudio = 3  # CD Audio format
	ppSoundFormatMIDI = 2  # MIDI format
	ppSoundFormatMixed = -2  # Mixed format
	ppSoundFormatNone = 0  # No format
	ppSoundFormatWAV = 1  # WAV format


@unique
class PpTabStopType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppTabStopCenter = 2  # Center tab stop
	ppTabStopDecimal = 4  # Decimal tab stop
	ppTabStopLeft = 1  # Left tab stop
	ppTabStopMixed = -2  # Mixed
	ppTabStopRight = 3  # Right tab stop


@unique
class PpTextLevelEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAnimateByAllLevels = 16  # By all levels
	ppAnimateByFifthLevel = 5  # By fifth level
	ppAnimateByFirstLevel = 1  # By first level
	ppAnimateByFourthLevel = 4  # By fourth level
	ppAnimateBySecondLevel = 2  # By second level
	ppAnimateByThirdLevel = 3  # By third level
	ppAnimateLevelMixed = -2  # Mixed level
	ppAnimateLevelNone = 0  # No level


@unique
class PpTextStyleType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppDefaultStyle = 1  # Default style
	ppTitleStyle = 2  # Title style
	ppBodyStyle = 3  # Body style
	

@unique
class PpTextUnitEffect(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppAnimateByCharacter = 2  # Text-unit effects are animated by character.
	ppAnimateByParagraph = 0  # Text-unit effects are animated by paragraph.
	ppAnimateByWord = 1  # Text-unit effects are animated by word.
	ppAnimateUnitMixed = -2  # Text-unit effects are animated in a mixed manner.


@unique
class PpTransitionSpeed(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppTransitionSpeedFast = 3  # Fast
	ppTransitionSpeedMedium = 2  # Medium
	ppTransitionSpeedMixed = -2  # Mixed
	ppTransitionSpeedSlow = 1  # Slow


@unique
class PpUpdateOption(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppUpdateOptionAutomatic = 2  # Link will be updated each time the presentation is opened or the source file changes.
	ppUpdateOptionManual = 1  # Link will be updated only when the user specifically asks to update the presentation.
	ppUpdateOptionMixed = -2  # Mixed


@unique
class PpViewType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppViewHandoutMaster = 4  # Handout Master
	ppViewMasterThumbnails = 12  # Master Thumbnails
	ppViewNormal = 9  # Normal
	ppViewNotesMaster = 5  # Notes Master
	ppViewNotesPage = 3  # Notes Page
	ppViewOutline = 6  # Outline
	ppViewPrintPreview = 10  # Print Preview
	ppViewSlide = 1  # Slide
	ppViewSlideMaster = 2  # Slide Master
	ppViewSlideSorter = 7  # Slide Sorter
	ppViewThumbnails = 11  # Thumbnails
	ppViewTitleMaster = 8  # Title Master


@unique
class PpWindowState(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	ppWindowMaximized = 3  # Maximized
	ppWindowMinimized = 2  # Minimized
	ppWindowNormal = 1  # Normal


@unique
class XlAxisCrosses(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAxisCrossesAutomatic = -4105  # Word sets the axis crossing point.
	xlAxisCrossesCustom = -4114  # The CrossesAt property specifies the axis crossing point.
	xlAxisCrossesMaximum = 2  # The axis crosses at the maximum value.
	xlAxisCrossesMinimum = 4  # The axis crosses at the minimum value.


@unique
class XlAxisGroup(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlPrimary = 1  # The primary axis group.
	xlSecondary = 2  # The secondary axis group.


@unique
class XlAxisType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlCategory = 1  # Axis displays categories.
	xlValue = 2  # Axis displays values.
	xlSeriesAxis = 3  # Axis displays data series.


@unique
class XlBackground(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlBackgroundAutomatic = -4105  # Word controls the background.
	xlBackgroundOpaque = 3  # An opaque background.
	xlBackgroundTransparent = 2  # A transparent background.


@unique
class XlBarShape(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlBox = 0  # A box.
	xlConeToMax = 5  # A cone, truncated at the specified value.
	xlConeToPoint = 4  # A cone, coming to a point at the specified value.
	xlCylinder = 3  # A cylinder.
	xlPyramidToMax = 2  # A pyramid, truncated at the specified value.
	xlPyramidToPoint = 1  # A pyramid, coming to a point at the specified value.


@unique
class XlBinsType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlBinsTypeAutomatic = 0  # Sets bins type automatically.
	xlBinsTypeCategorical = 1  # Sets bins type by category.
	xlBinsTypeManual = 2  # Sets bins type manually.
	xlBinsTypeBinSize = 3  # Sets bins type by size.
	xlBinsTypeBinCount = 4  # Sets bins type by count.


@unique
class XlBorderWeight(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlHairline = 1  # A hairline border (thinnest border).
	xlMedium = -4138  # A medium border.
	xlThick = 4  # A thick border (widest border).
	xlThin = 2  # A thin border.


@unique
class XlCategoryLabelLevel(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlCategoryLabelLevelAll = -1  # Use all category label levels within range on the chart. The default.
	xlCategoryLabelLevelCustom = -2  # Indicates literal data in the category labels.
	xlCategoryLabelLevelNone = -3  # Use no category labels in the chart. Defaults to automatic indexed labels.

@unique
class XlCategoryType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAutomaticScale = -4105  # Word controls the axis type.
	xlCategoryScale = 2  # Axis groups data by an arbitrary set of categories.
	xlTimeScale = 3  # Axis groups data on a time scale.


@unique
class XlChartElementPosition(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlChartElementPositionAutomatic = -4105  # Automatically sets the position of the chart element.
	xlChartElementPositionCustom = -4114  # Specifies a specific position for the chart element.


@unique
class XlChartGallery(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAnyGallery = 23  # Either of the galleries.
	xlBuiltIn = 21  # The built-in gallery.
	xlUserDefined = 22  # The user-defined gallery.


@unique
class XlChartItem(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAxis = 21  # Axis.
	xlAxisTitle = 17  # Axis title.
	xlChartArea = 2  # Chart area.
	xlChartTitle = 4  # Chart title.
	xlCorners = 6  # Corners.
	xlDataLabel = 0  # Data label.
	xlDataTable = 7  # Data table.
	xlDisplayUnitLabel = 30  # Display unit label.
	xlDownBars = 20  # Down bars.
	xlDropLines = 26  # Drop lines.
	xlErrorBars = 9  # Error bars.
	xlFloor = 23  # Floor.
	xlHiLoLines = 25  # HiLo lines.
	xlLeaderLines = 29  # Leader lines.
	xlLegend = 24  # Legend.
	xlLegendEntry = 12  # Legend entry.
	xlLegendKey = 13  # Legend key.
	xlMajorGridlines = 15  # Major gridlines.
	xlMinorGridlines = 16  # Minor gridlines.
	xlNothing = 28  # Nothing.
	xlPivotChartDropZone = 32  # PivotChart drop zone.
	xlPivotChartFieldButton = 31  # PivotChart field button.
	xlPlotArea = 19  # Plot area.
	xlRadarAxisLabels = 27  # Radar axis labels.
	xlSeries = 3  # Series.
	xlSeriesLines = 22  # Series lines.
	xlShape = 14  # Shape.
	xlTrendline = 8  # Trend line.
	xlUpBars = 18  # Up bars.
	xlWalls = 5  # Walls.
	xlXErrorBars = 10  # X error bars.
	xlYErrorBars = 11  # Y error bars.


@unique
class XlChartPicturePlacement(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAllFaces = 7  # Display on all faces.
	xlEnd = 2  # Display on end.
	xlEndSides = 3  # Display on end and sides.
	xlFront = 4  # Display on front.
	xlFrontEnd = 6  # Display on front and end.
	xlFrontSides = 5  # Display on front and sides.
	xlSides = 1  # Display on sides.


@unique
class XlChartPictureType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlStack = 2  # The picture is sized to repeat a maximum of 15 times in the longest stacked bar.
	xlStackScale = 3  # The picture is sized to a specified number of units and repeated the length of the bar.
	xlStretch = 1  # The picture is stretched the full length of the stacked bar.


@unique
class XlChartSplitType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlSplitByCustomSplit = 4  # The second chart displays arbitrary slides.
	xlSplitByPercentValue = 3  # The second chart displays values less than a percentage of the total value. The percentage is specified by the SplitValue property.
	xlSplitByPosition = 1  # The second chart displays the smallest values in the data series. The number of values to display is specified by the SplitValue property.
	xlSplitByValue = 2  # The second chart displays values less than the value specified by the SplitValue property.


@unique
class XlColorIndex(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlColorIndexAutomatic = -4105  # Automatic color.
	xlColorIndexNone = -4142  # No color.


# Not a unique enumeration
class XlConstants(Enum):
	"""
	Not a unique enumeration.
	"""
	xlTop = -4160  # Top.
	xlRight = -4152  # Right.
	xlNone = -4142  # Do not display error bars in the specified chart group or series.
	xlLow = -4134  # Low.
	xlLeft = -4131  # Left.
	xlJustify = -4130  # Justify.
	xlHigh = -4127  # High.
	xlGray75 = -4126  # 75% gray pattern.
	xlGray50 = -4125  # 50% gray pattern.
	xlGray25 = -4124  # 25% gray pattern.
	xlDistributed = -4117  # Distributed.
	xlCustom = -4114  # Word applies custom settings, such as a color or error amount, to the specified object.
	xlCombination = -4111  # Combination.
	xlCenter = -4108  # Center.
	xlBottom = -4107  # Bottom.
	xlAutomatic = -4105  # Word applies automatic settings, such as a color or page number, to the specified object.
	xl3DSurface = -4103  # Three-dimensional surface chart group or series.
	xl3DBar = -4099  # Three-dimensional bar chart group or series.
	xlDefaultAutoFormat = -1  # Word applies default or automatic formatting.
	xlAbove = 0  # The summary row is displayed above the specified range.
	xlBelow = 1  # The summary row is displayed below the specified range.
	xlBoth = 1  # Display positive and negative error bars in the specified chart group or series.
	xlFixedValue = 1  # Display error amounts as a fixed value.
	xlGeneral = 1  # General.
	xlSolid = 1  # Solid pattern.
	xlSquare = 1  # Square.
	xlBar = 2  # Two-dimensional bar chart group or series.
	xlCorner = 2  # Corner.
	xlDiamond = 2  # Diamond pattern.
	xlInside = 2  # Inside.
	xlMaximum = 2  # Maximum.
	xlPercent = 2  # Display error amounts as a percentage.
	xlPlusValues = 2  # Plus values.
	xlShowValue = 2  # Show value.
	xlSingle = 2  # Single line.
	xlTransparent = 2  # Transparent fill.
	xlColumn = 3  # Columnar chart group or series.
	xlMinusValues = 3  # Minus values.
	xlOpaque = 3  # Opaque fill.
	xlOutside = 3  # Outside.
	xlScale = 3  # Scale.
	xlShowPercent = 3  # Show percent.
	xlTriangle = 3  # Triangle.
	xlCross = 4  # Cross pattern.
	xlMinimum = 4  # Minimum.
	xlNextToAxis = 4  # Next to axis.
	xlShowLabel = 4  # Show label.
	xlStError = 4  # Display error amounts as a standard error.
	xlFill = 5  # Fill.
	xlShowLabelAndPercent = 5  # Show label and percent.
	xlStar = 5  # Star.
	xlCircle = 8  # Circle.
	xlChecker = 9  # Checker pattern.
	xlPlus = 9  # Display positive error bars in the specified chart group or series.
	xlSemiGray75 = 10  # 75% semi-gray pattern.
	xlLightHorizontal = 11  # Light horizontal line pattern.
	xlLightVertical = 12  # Light vertical line pattern.
	xlLightDown = 13  # Light down line pattern.
	xlLightUp = 14  # Light up line pattern.
	xlGrid = 15  # Grid pattern.
	xlCrissCross = 16  # Criss-cross pattern.
	xlGray16 = 17  # 16% gray pattern.
	xlGray8 = 18  # 8% gray pattern.


@unique
class XlCopyPictureFormat(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlBitmap = 2  # A bitmap (.bmp, .jpg, .gif).
	xlPicture = -4147  # A drawn picture (.png, .wmf, .mix).


@unique
class XlDataLabelPosition(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlLabelPositionAbove = 0  # The data label is positioned above the data point.
	xlLabelPositionBelow = 1  # The data label is positioned below the data point.
	xlLabelPositionBestFit = 5  # Word sets the position of the data label.
	xlLabelPositionCenter = -4108  # The data label is centered on the data point or is inside a bar or pie chart.
	xlLabelPositionCustom = 7  # The data label is in a custom position.
	xlLabelPositionInsideBase = 4  # The data label is positioned inside the data point at the bottom edge.
	xlLabelPositionInsideEnd = 3  # The data label is positioned inside the data point at the top edge.
	xlLabelPositionLeft = -4131  # The data label is positioned to the left of the data point.
	xlLabelPositionMixed = 6  # Data labels are in multiple positions.
	xlLabelPositionOutsideEnd = 2  # The data label is positioned outside the data point at the top edge.
	xlLabelPositionRight = -4152  # The data label is positioned to the right of the data point.


@unique
class XlDataLabelSeparator(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlDataLabelSeparatorDefault = 1  # Word selects the separator.


@unique
class XlDataLabelsType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlDataLabelsShowBubbleSizes = 6  # Show the size of the bubble in reference to the absolute value.
	xlDataLabelsShowLabel = 4  # The category for the point.
	xlDataLabelsShowLabelAndPercent = 5  # The percentage of the total, and the category for the point. Available only for pie charts and doughnut charts.
	xlDataLabelsShowNone = -4142  # No data labels.
	xlDataLabelsShowPercent = 3  # The percentage of the total. Available only for pie charts and doughnut charts.
	xlDataLabelsShowValue = 2  # The default value for the point (assumed if this argument is not specified).


@unique
class XlDisplayBlanksAs(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlInterpolated = 3  # Values are interpolated into the chart.
	xlNotPlotted = 1  # Blank cells are not plotted.
	xlZero = 2  # Blanks are plotted as zero.


@unique
class XlDisplayUnit(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlHundredMillions = -8  # Hundreds of millions.
	xlHundreds = -2  # Hundreds.
	xlHundredThousands = -5  # Hundreds of thousands.
	xlMillionMillions = -10  # Millions of millions.
	xlMillions = -6  # Millions.
	xlTenMillions = -7  # Tens of millions.
	xlTenThousands = -4  # Tens of thousands.
	xlThousandMillions = -9  # Thousands of millions.
	xlThousands = -3  # Thousands.


@unique
class XlEndStyleCap(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlCap = 1  # Caps are applied.
	xlNoCap = 2  # No caps are applied.


@unique
class XlErrorBarDirection(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlChartX = -4168  # Bars run parallel to the y-axis for x-axis values.
	xlChartY = 1  # Bars run parallel to the x-axis for y-axis values.


@unique
class XlErrorBarInclude(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlErrorBarIncludeBoth = 1  # Both the positive and negative error range.
	xlErrorBarIncludeMinusValues = 3  # Only the negative error range.
	xlErrorBarIncludeNone = -4142  # No error bar range.
	xlErrorBarIncludePlusValues = 2  # Only the positive error range.


@unique
class XlErrorBarType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlErrorBarTypeCustom = -4114  # The range is set by fixed values or cell values.
	xlErrorBarTypeFixedValue = 1  # Fixed-length error bars.
	xlErrorBarTypePercent = 2  # The percentage of the range to be covered by the error bars.
	xlErrorBarTypeStDev = -4155  # Shows the range for a specified number of standard deviations.
	xlErrorBarTypeStError = 4  # Shows the standard error range.


@unique
class XlHAlign(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlHAlignCenter = -4108  # Center.
	xlHAlignCenterAcrossSelection = 7  # Center across selection.
	xlHAlignDistributed = -4117  # Distribute.
	xlHAlignFill = 5  # Fill.
	xlHAlignGeneral = 1  # Align according to data type.
	xlHAlignJustify = -4130  # Justify.
	xlHAlignLeft = -4131  # Left.
	xlHAlignRight = -4152  # Right.


@unique
class XlLegendPosition(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlLegendPositionBottom = -4107  # Below the chart.
	xlLegendPositionCorner = 2  # In the upper-right corner of the chart border.
	xlLegendPositionCustom = -4161  # A custom position.
	xlLegendPositionLeft = -4131  # Left of the chart.
	xlLegendPositionRight = -4152  # Right of the chart.
	xlLegendPositionTop = -4160  # Above the chart.


@unique
class XlLineStyle(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlContinuous = 1  # A continuous line.
	xlDash = -4115  # A dashed line.
	xlDashDot = 4  # Alternating dashes and dots.
	xlDashDotDot = 5  # A dash followed by two dots.
	xlDot = -4118  # A dotted line.
	xlDouble = -4119  # A double line.
	xlLineStyleNone = -4142  # No line.
	xlSlantDashDot = 13  # Slanted dashes.


@unique
class XlMarkerStyle(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlMarkerStyleAutomatic = -4105  # Automatic markers.
	xlMarkerStyleCircle = 8  # Circular markers.
	xlMarkerStyleDash = -4115  # Long bar markers.
	xlMarkerStyleDiamond = 2  # Diamond-shaped markers.
	xlMarkerStyleDot = -4118  # Short bar markers.
	xlMarkerStyleNone = -4142  # No markers.
	xlMarkerStylePicture = -4147  # Picture markers.
	xlMarkerStylePlus = 9  # Square markers with a plus sign.
	xlMarkerStyleSquare = 1  # Square markers.
	xlMarkerStyleStar = 5  # Square markers with an asterisk.
	xlMarkerStyleTriangle = 3  # Triangular markers.
	xlMarkerStyleX = -4168  # Square markers with an X.


@unique
class XlOrientation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlDownward = -4170  # Text runs downward.
	xlHorizontal = -4128  # Text runs horizontally.
	xlUpward = -4171  # Text runs upward.
	xlVertical = -4166  # Text runs downward and is centered in the cell.


@unique
class XlParentDataLabelOptions(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlParentDataLabelOptionsNone = 0  # No parent labels are shown.
	xlParentDataLabelOptionsBanner = 1  # The parent label layout is a banner above the category.
	xlParentDataLabelOptionsOverlapping = 2  # The parent label is laid out within the category.


@unique
class XlPattern(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlPatternAutomatic = -4105  # Word controls the pattern.
	xlPatternChecker = 9  # A checkerboard.
	xlPatternCrissCross = 16  # Criss-crossed lines.
	xlPatternDown = -4121  # Dark diagonal lines running from the upper-left to the lower-right.
	xlPatternGray16 = 17  # 16% gray.
	xlPatternGray25 = -4124  # 25% gray.
	xlPatternGray50 = -4125  # 50% gray.
	xlPatternGray75 = -4126  # 75% gray.
	xlPatternGray8 = 18  # 8% gray.
	xlPatternGrid = 15  # A grid.
	xlPatternHorizontal = -4128  # Dark horizontal lines.
	xlPatternLightDown = 13  # Light diagonal lines running from the upper-left to the lower-right.
	xlPatternLightHorizontal = 11  # Light horizontal lines.
	xlPatternLightUp = 14  # Light diagonal lines running from the lower-left to the upper-right.
	xlPatternLightVertical = 12  # Light vertical bars.
	xlPatternLinearGradient = 4000  # A linear gradient.
	xlPatternNone = -4142  # No pattern.
	xlPatternRectangularGradient = 4001  # A rectangular gradient.
	xlPatternSemiGray75 = 10  # 75% dark moiré.
	xlPatternSolid = 1  # A solid color.
	xlPatternUp = -4162  # Dark diagonal lines running from the lower-left to the upper-right.
	xlPatternVertical = -4166  # Dark vertical bars.


@unique
class XlPictureAppearance(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlPrinter = 2  # The picture is copied as it will look when it is printed.
	xlScreen = 1  # The picture is copied to resemble its display on the screen as closely as possible.


@unique
class XlPieSliceIndex(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlCenterPoint = 5  # The center point of a pie slice.
	xlInnerCenterPoint = 8  # The innermost center point of a doughnut slice.
	xlInnerClockwisePoint = 7  # The innermost point of the most clockwise radius of a doughnut slice.
	xlInnerCounterClockwisePoint = 9  # The innermost point of the most counterclockwise radius of a doughnut slice.
	xlMidClockwiseRadiusPoint = 4  # The midpoint of the most clockwise radius of a slice.
	xlMidCounterClockwiseRadiusPoint = 6  # The midpoint of the most counterclockwise radius of a slice.
	xlOuterCenterPoint = 2  # The outer center point of the circumference of a slice.
	xlOuterClockwisePoint = 3  # The outermost clockwise point of the circumference of a slice.
	xlOuterCounterClockwisePoint = 1  # The outermost counterclockwise point of the circumference of a slice.


@unique
class XlPieSliceLocation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlCenterPoint = 5  # The center point of a pie slice.
	xlInnerCenterPoint = 8  # The innermost center point of a doughnut slice.
	xlInnerClockwisePoint = 7  # The innermost point of the most clockwise radius of a doughnut slice.
	xlInnerCounterClockwisePoint = 9  # The innermost point of the most counterclockwise radius of a doughnut slice.
	xlMidClockwiseRadiusPoint = 4  # The midpoint of the most clockwise radius of a slice.
	xlMidCounterClockwiseRadiusPoint = 6  # The midpoint of the most counterclockwise radius of a slice.
	xlOuterCenterPoint = 2  # The outer center point of the circumference of a slice.
	xlOuterClockwisePoint = 3  # The outermost clockwise point of the circumference of a slice.
	xlOuterCounterClockwisePoint = 1  # The outermost counterclockwise point of the circumference of a slice.


@unique
class XlPivotFieldOrientation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlColumnField = 2  # A column field.
	xlDataField = 4  # A data field.
	xlHidden = 0  # A hidden field.
	xlPageField = 3  # A page field.
	xlRowField = 1  # A row field.


@unique
class XlReadingOrder(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlContext = -5002  # According to context.
	xlLTR = -5003  # Left-to-right.
	xlRTL = -5004  # Right-to-left.


@unique
class XlRgbColor(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlAliceBlue = 16775408  # Alice Blue
	xlAntiqueWhite = 14150650  # Antique White
	xlAqua = 16776960  # Aqua
	xlAquamarine = 13959039  # Aquamarine
	xlAzure = 16777200  # Azure
	xlBeige = 14480885  # Beige
	xlBisque = 12903679  # Bisque
	xlBlack = 0  # Black
	xlBlanchedAlmond = 13495295  # Blanched Almond
	xlBlue = 16711680  # Blue
	xlBlueViolet = 14822282  # Blue Violet
	xlBrown = 2763429  # Brown
	xlBurlyWood = 8894686  # Burly Wood
	xlCadetBlue = 10526303  # Cadet Blue
	xlChartreuse = 65407  # Chartreuse
	xlCoral = 5275647  # Coral
	xlCornflowerBlue = 15570276  # Cornflower Blue
	xlCornsilk = 14481663  # Cornsilk
	xlCrimson = 3937500  # Crimson
	xlDarkBlue = 9109504  # Dark Blue
	xlDarkCyan = 9145088  # Dark Cyan
	xlDarkGoldenrod = 755384  # Dark Goldenrod
	xlDarkGreen = 25600  # Dark Green
	xlDarkGrey = 11119017  # Dark Grey
	xlDarkKhaki = 7059389  # Dark Khaki
	xlDarkMagenta = 9109643  # Dark Magenta
	xlDarkOliveGreen = 3107669  # Dark Olive Green
	xlDarkOrange = 36095  # Dark Orange
	xlDarkOrchid = 13382297  # Dark Orchid
	xlDarkRed = 139  # Dark Red
	xlDarkSalmon = 8034025  # Dark Salmon
	xlDarkSeaGreen = 9419919  # Dark Sea Green
	xlDarkSlateBlue = 9125192  # Dark Slate Blue
	xlDarkSlateGrey = 5197615  # Dark Slate Grey
	xlDarkTurquoise = 13749760  # Dark Turquoise
	xlDarkViolet = 13828244  # Dark Violet
	xlDeepPink = 9639167  # Deep Pink
	xlDeepSkyBlue = 16760576  # Deep Sky Blue
	xlDimGray = 6908265  # Dim Gray
	xlDodgerBlue = 16748574  # Dodger Blue
	xlFireBrick = 2237106  # Fire Brick
	xlFloralWhite = 15792895  # Floral White
	xlForestGreen = 2263842  # Forest Green
	xlFuchsia = 16711935  # Fuchsia
	xlGainsboro = 14474460  # Gainsboro
	xlGhostWhite = 16775416  # Ghost White
	xlGold = 55295  # Gold
	xlGoldenrod = 2139610  # Goldenrod
	xlGreen = 32768  # Green
	xlGreenYellow = 3145645  # Green Yellow
	xlGrey = 8421504  # Grey
	xlHoneydew = 15794160  # Honeydew
	xlHotPink = 11823615  # Hot Pink
	xlIndianRed = 6053069  # Indian Red
	xlIndigo = 8519755  # Indigo
	xlIvory = 15794175  # Ivory
	xlKhaki = 9234160  # Khaki
	xlLavender = 16443110  # Lavender
	xlLavenderBlush = 16118015  # Lavender Blush
	xlLawnGreen = 64636  # Lawn Green
	xlLemonChiffon = 13499135  # Lemon Chiffon
	xlLightBlue = 15128749  # Light Blue
	xlLightCoral = 8421616  # Light Coral
	xlLightGoldenrodYellow = 13826810  # LightGoldenrodYellow
	xlLightGreen = 9498256  # Light Green
	xlLightGrey = 13882323  # Light Grey
	xlLightPink = 12695295  # Light Pink
	xlLightSalmon = 8036607  # Light Salmon
	xlLightSeaGreen = 11186720  # Light Sea Green
	xlLightSkyBlue = 16436871  # Light Sky Blue
	xlLightSlateGray = 10061943  # Light Slate Gray
	xlLightSteelBlue = 14599344  # Light Steel Blue
	xlLightYellow = 14745599  # Light Yellow
	xlLime = 65280  # Lime
	xlLimeGreen = 3329330  # Lime Green
	xlLinen = 15134970  # Linen
	xlMaroon = 128  # Maroon
	xlMediumAquamarine = 11206502  # Medium Aquamarine
	xlMediumBlue = 13434880  # Medium Blue
	xlMediumOrchid = 13850042  # Medium Orchid
	xlMediumPurple = 14381203  # Medium Purple
	xlMediumSeaGreen = 7451452  # Medium Sea Green
	xlMediumSlateBlue = 15624315  # Medium Slate Blue
	xlMediumSpringGreen = 10156544  # Medium Spring Green
	xlMediumTurquoise = 13422920  # Medium Turquoise
	xlMediumVioletRed = 8721863  # Medium Violet Red
	xlMidnightBlue = 7346457  # Midnight Blue
	xlMintCream = 16449525  # Mint Cream
	xlMistyRose = 14804223  # Misty Rose
	xlMoccasin = 11920639  # Moccasin
	xlNavajoWhite = 11394815  # Navajo White
	xlNavy = 8388608  # Navy
	xlOldLace = 15136253  # Old Lace
	xlOlive = 32896  # Olive
	xlOliveDrab = 2330219  # Olive Drab
	xlOrange = 42495  # Orange
	xlOrangeRed = 17919  # Orange Red
	xlOrchid = 14053594  # Orchid
	xlPaleGoldenrod = 7071982  # Pale Goldenrod
	xlPaleGreen = 10025880  # Pale Green
	xlPaleTurquoise = 15658671  # Pale Turquoise
	xlPaleVioletRed = 9662683  # Pale Violet Red
	xlPapayaWhip = 14020607  # Papaya Whip
	xlPeachPuff = 12180223  # Peach Puff
	xlPeru = 4163021  # Peru
	xlPink = 13353215  # Pink
	xlPlum = 14524637  # Plum
	xlPowderBlue = 15130800  # Powder Blue
	xlPurple = 8388736  # Purple
	xlRed = 255  # Red
	xlRosyBrown = 9408444  # Rosy Brown
	xlRoyalBlue = 14772545  # Royal Blue
	xlSalmon = 7504122  # Salmon
	xlSandyBrown = 6333684  # Sandy Brown
	xlSeaGreen = 5737262  # Sea Green
	xlSeashell = 15660543  # Seashell
	xlSienna = 2970272  # Sienna
	xlSilver = 12632256  # Silver
	xlSkyBlue = 15453831  # Sky Blue
	xlSlateBlue = 13458026  # Slate Blue
	xlSlateGrey = 9470064  # Slate Grey
	xlSnow = 16448255  # Snow
	xlSpringGreen = 8388352  # Spring Green
	xlSteelBlue = 11829830  # Steel Blue
	xlTan = 9221330  # Tan
	xlTeal = 8421376  # Teal
	xlThistle = 14204888  # Thistle
	xlTomato = 4678655  # Tomato
	xlTurquoise = 13688896  # Turquoise
	xlViolet = 15631086  # Violet
	xlWheat = 11788021  # Wheat
	xlWhite = 16777215  # White
	xlWhiteSmoke = 16119285  # White Smoke
	xlYellow = 65535  # Yellow
	xlYellowGreen = 3329434  # Yellow Green


@unique
class XlRowCol(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlColumns = 2  # The data series is in a row.
	xlRows = 1  # The data series is in a column.


@unique
class XlScaleType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlScaleLinear = -4132  # A linear scale.
	xlScaleLogarithmic = -4133  # A logarithmic scale.


@unique
class XlSeriesNameLevel(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlSeriesNameLevelAll = -1  # Sets series names to all series name levels within range on the chart. The default.
	xlSeriesNameLevelCustom = -2  # Indicates literal data in the series names.
	xlSeriesNameLevelNone = -3  # Sets no series names in the chart.


@unique
class XlSizeRepresents(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlSizeIsArea = 1  # The area of the bubble.
	xlSizeIsWidth = 2  # The width of the bubble.


@unique
class XlTickLabelOrientation(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlTickLabelOrientationAutomatic = -4105  # The text orientation is set by Microsoft Word.
	xlTickLabelOrientationDownward = -4170  # The text runs downward.
	xlTickLabelOrientationHorizontal = -4128  # The characters run horizontally.
	xlTickLabelOrientationUpward = -4171  # The text runs upward.
	xlTickLabelOrientationVertical = -4166  # The characters run vertically.


@unique
class XlTickLabelPosition(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlTickLabelPositionHigh = -4127  # The top or right side of the chart.
	xlTickLabelPositionLow = -4134  # The bottom or left side of the chart.
	xlTickLabelPositionNextToAxis = 4  # Next to the axis (where the axis is not at either side of the chart).
	xlTickLabelPositionNone = -4142  # No tick marks.


@unique
class XlTickMark(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlTickMarkCross = 4  # Crosses the axis.
	xlTickMarkInside = 2  # Inside the axis.
	xlTickMarkNone = -4142  # No mark.
	xlTickMarkOutside = 3  # Outside the axis.


@unique
class XlTimeUnit(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlDays = 0  # Days
	xlMonths = 1  # Months
	xlYears = 2  # Years


@unique
class XlTrendlineType(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlExponential = 5  # Uses an equation to calculate the least squares fit through points (for example, y=ab^x) .
	xlLinear = -4132  # Uses the linear equation y = mx + b to calculate the least squares fit through points.
	xlLogarithmic = -4133  # Uses the equation y = c ln x + b to calculate the least squares fit through points.
	xlMovingAvg = 6  # Uses a sequence of averages computed from parts of the data series. The number of points equals the total number of points in the series minus the number specified for the period.
	xlPolynomial = 3  # Uses an equation to calculate the least squares fit through points (for example, y = ax^6 + bx^5 + cx^4 + dx^3 + ex^2 + fx + g).
	xlPower = 4  # Uses an equation to calculate the least squares fit through points (for example, y = ax^b).


@unique
class XlVAlign(Enum):
	"""
	@Enum: inherets methods from the Enum class
	"""
	
	xlVAlignBottom = -4107  # Bottom alignment.
	xlVAlignCenter = -4108  # Center alignment.
	xlVAlignDistributed = -4117  # Distributed alignment.
	xlVAlignJustify = -4130  # Justified alignment.
	xlVAlignTop = -4160  # Top alignment.
