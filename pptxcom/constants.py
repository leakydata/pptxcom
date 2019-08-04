class MsoAnimAccumulate:
	msoAnimAccumulateAlways = 2  # Accumulates with other animation behaviors.
	msoAnimAccumulateNone = 1  # Does not accumulate.


class MsoAnimAdditive:
	msoAnimAdditiveAddBase = 1  # Uses the animation behavior of the base animations.
	msoAnimAdditiveAddSum = 2  # Adds together the animation behavior of multiple animations.


class MsoAnimAfterEffect:
	msoAnimAfterEffectDim = 1  # Dimmed
	msoAnimAfterEffectHide = 2  # Hidden
	msoAnimAfterEffectHideOnNextClick = 3  # Hidden on the next mouse click
	msoAnimAfterEffectMixed = -1  # Mixed
	msoAnimAfterEffectNone = 0  # Unchanged


class MsoAnimateByLevel:
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


class MsoAnimCommandType:
	msoAnimCommandTypeCall = 1  # Call
	msoAnimCommandTypeEvent = 0  # Event
	msoAnimCommandTypeVerb = 2  # Verb


class MsoAnimDirection:
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


class MsoAnimEffect:
	msoAnimEffectAppear = 1  # Appears
	msoAnimEffectArcUp = 47  # Arcs Up
	msoAnimEffectAscend = 39  # Ascends
	msoAnimEffectBlast = 64  # Blasts
	msoAnimEffectBlinds = 3  # Blinds
	msoAnimEffectBoldFlash = 63  # Bold Flash
	msoAnimEffectBoldReveal = 65  # Bold Reveals
	msoAnimEffectBoomerang = 25  # Boomerangs
	msoAnimEffectBounce = 26  # Bounce
	msoAnimEffectBox = 4  # Box
	msoAnimEffectBrushOnColor = 66  # Brush on Color
	msoAnimEffectBrushOnUnderline = 67  # Brush on Underline
	msoAnimEffectCenterRevolve = 40  # Center Revolves
	msoAnimEffectChangeFillColor = 54  # FillColor Changes
	msoAnimEffectChangeFont = 55  # Font Changes
	msoAnimEffectChangeFontColor = 56  # Font Color Changes
	msoAnimEffectChangeFontSize = 57  # Font Size Changes
	msoAnimEffectChangeFontStyle = 58  # Font Style Changes
	msoAnimEffectChangeLineColor = 60  # Line color Changes
	msoAnimEffectCheckerboard = 5  # Checkerboard Effect
	msoAnimEffectCircle = 6  # Circle
	msoAnimEffectColorBlend = 68  # Color Bleeds
	msoAnimEffectColorReveal = 27  # Color Revealed
	msoAnimEffectColorWave = 69  # Color Wave
	msoAnimEffectComplementaryColor = 70  # Complementary Color
	msoAnimEffectComplementaryColor2 = 71  # Complementary Color2
	msoAnimEffectContrastingColor = 72  # Contrasting Color
	msoAnimEffectCrawl = 7  # Crawl Effect
	msoAnimEffectCredits = 28  # Credits Effect
	msoAnimEffectCustom = 0  # Custom Effect
	msoAnimEffectDarken = 73  # Darken Effect
	msoAnimEffectDesaturate = 74  # Desaturate Effect
	msoAnimEffectDescend = 42  # Descend Effect
	msoAnimEffectDiamond = 8  # Diamond Effect
	msoAnimEffectDissolve = 9  # Dissolve Effect
	msoAnimEffectEaseIn = 29  # EaseIn Effect
	msoAnimEffectExpand = 50  # Expand Effect
	msoAnimEffectFade = 10  # Fade Effect
	msoAnimEffectFadedSwivel = 41  # Faded Swivel Effect
	msoAnimEffectFadedZoom = 48  # Faded Zoom Effect
	msoAnimEffectFlashBulb = 75  # Flash Bulb Effect
	msoAnimEffectFlashOnce = 11  # Flash Once
	msoAnimEffectFlicker = 76  # Flicker Effect
	msoAnimEffectFlip = 51  # Flip Effect
	msoAnimEffectFloat = 30  # Float Effect
	msoAnimEffectFly = 2  # Fly Effect
	msoAnimEffectFold = 53  # Fold Effect
	msoAnimEffectGlide = 49  # Glide Effect
	msoAnimEffectGrowAndTurn = 31  # Grow and Turn Effect
	msoAnimEffectGrowShrink = 59  # Grow and Shrink Effect
	msoAnimEffectGrowWithColor = 77  # Grow with Color Effect
	msoAnimEffectLighten = 78  # Lighten Effect
	msoAnimEffectLightSpeed = 32  # Light Speed Effect
	msoAnimEffectMediaPause = 84  # Media Pause Effect
	msoAnimEffectMediaPlay = 83  # Media Play Effect
	msoAnimEffectMediaStop = 85  # Media Stop Effect
	msoAnimEffectPath4PointStar = 101  # Path4PointStar Effect
	msoAnimEffectPath5PointStar = 90  # Path5PointStar Effect
	msoAnimEffectPath6PointStar = 96  # Path6PointStar Effect
	msoAnimEffectPath8PointStar = 102  # Path8PointStar Effect
	msoAnimEffectPathArcDown = 122  # Moves on the Arc Down path
	msoAnimEffectPathArcLeft = 136  # Moves on the Arc Left path
	msoAnimEffectPathArcRight = 143  # Moves on the Arc Right Path
	msoAnimEffectPathArcUp = 129  # Moves on the Arc Up path
	msoAnimEffectPathBean = 116  # Moves on the Bean path
	msoAnimEffectPathBounceLeft = 126  # Moves on the Bounce Left path
	msoAnimEffectPathBounceRight = 139  # Moves on the Bounce Right path
	msoAnimEffectPathBuzzsaw = 110  # Moves on the Buzzsaw path
	msoAnimEffectPathCircle = 86  # Moves on a Circular Path
	msoAnimEffectPathCrescentMoon = 91  # Moves on a Crescent Moon path
	msoAnimEffectPathCurvedSquare = 105  # Moves on a CurvedSquare path
	msoAnimEffectPathCurvedX = 106  # Moves on a Curved X path
	msoAnimEffectPathCurvyLeft = 133  # Moves on a Curvy Left path
	msoAnimEffectPathCurvyRight = 146  # Moves on a Curvy Right path
	msoAnimEffectPathCurvyStar = 108  # Moves on a Curvy Star path
	msoAnimEffectPathDecayingWave = 145  # Moves on a Decaying Wave path
	msoAnimEffectPathDiagonalDownRight = 134  # Moves on a Diagonal Down-Right path
	msoAnimEffectPathDiagonalUpRight = 141  # Moves on a Diagonal Up-Right path
	msoAnimEffectPathDiamond = 88  # Moves on a Diamond path
	msoAnimEffectPathDown = 127  # Moves on a Down path
	msoAnimEffectPathEqualTriangle = 98  # Moves on a equilateral triangle path
	msoAnimEffectPathFigure8Four = 113  # Moves on a Figure8Four path
	msoAnimEffectPathFootball = 97  # Moves on a Football path
	msoAnimEffectPathFunnel = 137  # Moves on a Funnel path
	msoAnimEffectPathHeart = 94  # Moves on a Heart shape path
	msoAnimEffectPathHeartbeat = 130  # Moves on a Heart Beat path
	msoAnimEffectPathHexagon = 89  # Moves on a Hexagon path
	msoAnimEffectPathHorizontalFigure8 = 111  # Moves on a Horizontal Figure8 path
	msoAnimEffectPathInvertedSquare = 119  # Moves on a Inverted Square path
	msoAnimEffectPathInvertedTriangle = 118  # Moves on a Inverted Triangle path
	msoAnimEffectPathLeft = 120  # Moves on a Left path
	msoAnimEffectPathLoopdeLoop = 109  # Moves on a LoopdeLoop path
	msoAnimEffectPathNeutron = 114  # Moves on a Neutron path
	msoAnimEffectPathOctagon = 95  # Moves on a Octagon path
	msoAnimEffectPathParallelogram = 99  # Moves on a Parallelogram path
	msoAnimEffectPathPeanut = 112  # Moves on a Peanut path
	msoAnimEffectPathPentagon = 100  # Moves on a Pentagon path
	msoAnimEffectPathPlus = 117  # Moves on a Plus path
	msoAnimEffectPathPointyStar = 104  # Moves on a PointyStar path
	msoAnimEffectPathRight = 149  # Moves on a Right path
	msoAnimEffectPathRightTriangle = 87  # Moves on a RightTriangle path
	msoAnimEffectPathSCurve1 = 144  # Moves on a SCurve1 path
	msoAnimEffectPathSCurve2 = 124  # Moves on a SCurve2 path
	msoAnimEffectPathSineWave = 125  # Moves on a SineWave path
	msoAnimEffectPathSpiralLeft = 140  # Moves on a SpiralLeft path
	msoAnimEffectPathSpiralRight = 131  # Moves on a SpiralRight path
	msoAnimEffectPathSpring = 138  # Moves on a Spring path
	msoAnimEffectPathSquare = 92  # Moves on a Square path
	msoAnimEffectPathStairsDown = 147  # Moves on a StairsDown path
	msoAnimEffectPathSwoosh = 115  # Moves on a Swoosh path
	msoAnimEffectPathTeardrop = 103  # Moves on a Teardrop path
	msoAnimEffectPathTrapezoid = 93  # Moves on a Trapezoid path
	msoAnimEffectPathTurnDown = 135  # Moves on a TurnDown path
	msoAnimEffectPathTurnRight = 121  # Moves on a TurnRight path
	msoAnimEffectPathTurnUp = 128  # Moves on a TurnUp path
	msoAnimEffectPathTurnUpRight = 142  # Moves on a TurnUpRight path
	msoAnimEffectPathUp = 148  # Moves on an Up path
	msoAnimEffectPathVerticalFigure8 = 107  # Moves on a VerticalFigure8 path
	msoAnimEffectPathWave = 132  # Moves on a Wave path
	msoAnimEffectPathZigzag = 123  # Moves on a Zigzag path
	msoAnimEffectPeek = 12  # Peek effect
	msoAnimEffectPinwheel = 33  # Pinwel effect
	msoAnimEffectPlus = 13  # Plus effect
	msoAnimEffectRandomBars = 14  # Random Bars effect
	msoAnimEffectRandomEffects = 24  # Random effects
	msoAnimEffectRiseUp = 34  # Rise Up effect
	msoAnimEffectShimmer = 52  # Shimmer effect
	msoAnimEffectSling = 43  # Sling effect
	msoAnimEffectSpin = 61  # Spin effect
	msoAnimEffectSpinner = 44  # Spinner effect
	msoAnimEffectSpiral = 15  # Spiral effect
	msoAnimEffectSplit = 16  # Split effect
	msoAnimEffectStretch = 17  # Stretch effect
	msoAnimEffectStretchy = 45  # Stretchy effect
	msoAnimEffectStrips = 18  # Strips effect
	msoAnimEffectStyleEmphasis = 79  # Emphasis effect
	msoAnimEffectSwish = 35  # Swish effect
	msoAnimEffectSwivel = 19  # Swivel effect
	msoAnimEffectTeeter = 80  # Teeter effect
	msoAnimEffectThinLine = 36  # Thin line effect
	msoAnimEffectTransparency = 62  # Transparency effect
	msoAnimEffectUnfold = 37  # Unfold effect
	msoAnimEffectVerticalGrow = 81  # Vertical Grow effect
	msoAnimEffectWave = 82  # Wave effect
	msoAnimEffectWedge = 20  # Wedge effect
	msoAnimEffectWheel = 21  # Wheel effect
	msoAnimEffectWhip = 38  # Whip effect
	msoAnimEffectWipe = 22  # Wipe effect
	msoAnimEffectZip = 46  # Zip effect
	msoAnimEffectZoom = 23  # Zoom effect


class MsoAnimEffectAfter:
	msoAnimEffectAfterFreeze = 1  # After freeze.
	msoAnimEffectAfterHold = 3  # After hold.
	msoAnimEffectAfterRemove = 2  # After remove.
	msoAnimEffectAfterTransition = 4  # After transition.


class MsoAnimEffectRestart:
	msoAnimEffectRestartAlways = 1  # Always restarts.
	msoAnimEffectRestartNever = 3  # Never restarts.
	msoAnimEffectRestartWhenOff = 2  # Restarts when animation is off.


class MsoAnimFilterEffectSubtype:
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


class MsoAnimFilterEffectType:
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


class MsoAnimProperty:
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


class MsoAnimTextUnitEffect:
	msoAnimTextUnitEffectByCharacter = 1  # By character.
	msoAnimTextUnitEffectByParagraph = 0  # By paragraph.
	msoAnimTextUnitEffectByWord = 2  # By word.
	msoAnimTextUnitEffectMixed = -1  # Mixed effect.


class MsoAnimTriggerType:
	msoAnimTriggerAfterPrevious = 3  # After the Previous button is clicked.
	msoAnimTriggerMixed = -1  # Mixed actions.
	msoAnimTriggerNone = 0  # No action associated as the trigger.
	msoAnimTriggerOnPageClick = 1  # When a page is clicked.
	msoAnimTriggerOnShapeClick = 4  # When a shape is clicked.
	msoAnimTriggerWithPrevious = 2  # When the Previous button is clicked.


class MsoAnimType:
	msoAnimTypeColor = 2  # Color
	msoAnimTypeCommand = 6  # Command
	msoAnimTypeFilter = 7  # Filter
	msoAnimTypeMixed = -2  # Mixed
	msoAnimTypeMotion = 1  # Motion
	msoAnimTypeNone = 0  # None
	msoAnimTypeProperty = 5  # Property
	msoAnimTypeRotation = 4  # Rotation
	msoAnimTypeScale = 3  # Scale
	msoAnimTypeSet = 8  # Set


class MsoClickState:
	msoClickStateAfterAllAnimations = -2  # After all animations.
	msoClickStateBeforeAutomaticAnimations = -1  # Before automatic animations.


class msoShapeType:
	msoAutoShape = 1  # AutoShape (1)
	msoCallout = 2  # Callout (2)
	msoCanvas = 20  # Canvas (20)
	msoChart = 3  # Chart (3)
	msoComment = 4  # Comment (4)
	msoDiagram = 21  # Diagram (21)
	msoEmbeddedOLEObject = 7  # EmbeddedOLEObject (7)
	msoFormControl = 8  # FormControl (8)
	msoFreeform = 5  # Freeform (5)
	msoGroup = 6  # Group (6)
	msoInk = 22  # Ink (22)
	msoInkComment = 23  # InkComment (23)
	msoLine = 9  # Line (9)
	msoLinkedOLEObject = 10  # LinkedOLEObject (10)
	msoLinkedPicture = 11  # LinkedPicture (11)
	msoMedia = 16  # Media (16)
	msoOLEControlObject = 12  # OLEControlObject (12)
	msoPicture = 13  # Picture (13)
	msoPlaceholder = 14  # Placeholder (14)
	msoScriptAnchor = 18  # ScriptAnchor (18)
	msoShapeTypeMixed = -2  # ShapeTypeMixed (-2)
	msoTable = 19  # Table (19)
	msoTextBox = 17  # TextBox (17)
	msoTextEffect = 15  # TextEffect (15)


class PpActionType:
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


class PpAdvanceMode:
	ppAdvanceModeMixed = -2  # Mixed mode.
	ppAdvanceOnClick = 1  # Only when clicked.
	ppAdvanceOnTime = 2  # Automatically after a specified amount of time.


class PpAfterEffect:
	ppAfterEffectDim = 2  # Appears dimmed
	ppAfterEffectHide = 1  # Hides
	ppAfterEffectHideOnClick = 3  # Hidden when clicked
	ppAfterEffectMixed = -2  # Mixed effect
	ppAfterEffectNothing = 0  # No effect


class PpAlertLevel:
	ppAlertsAll = 2  # All alerts displayed.
	ppAlertsNone = 1  # No alerts displayed.


class PpArrangeStyle:
	ppArrangeCascade = 2  # Cascade
	ppArrangeTiled = 1  # Tiled


class PpAutoSize:
	ppAutoSizeMixed = -2  # Mixed size.
	ppAutoSizeNone = 0  # Does not change size.
	ppAutoSizeShapeToFitText = 1  # Auto sizes the shape to fit the text.


class PpBaselineAlignment:
	ppBaselineAlignBaseline = 1  # Aligned to the baseline.
	ppBaselineAlignCenter = 3  # Aligned to the center.
	ppBaselineAlignFarEast50 = 4  # Align FarEast50.
	ppBaselineAlignMixed = -2  # Mixed alignment.
	ppBaselineAlignTop = 2  # Aligned to the top.


class PpBorderType:
	ppBorderBottom = 3  # Bottom
	ppBorderDiagonalDown = 5  # Diagonally down
	ppBorderDiagonalUp = 6  # Diagonally up
	ppBorderLeft = 2  # Left
	ppBorderRight = 4  # Right
	ppBorderTop = 1  # Top
	ppBorderBottom = 3  # Bottom
	ppBorderDiagonalDown = 5  # Diagonally down
	ppBorderDiagonalUp = 6  # Diagonally up
	ppBorderLeft = 2  # Left
	ppBorderRight = 4  # Right
	ppBorderTop = 1  # Top


class PpBulletType:
	ppBulletMixed = -2  # Mixed bullets
	ppBulletNone = 0  # No bullets
	ppBulletNumbered = 2  # Numbered bullets
	ppBulletPicture = 3  # Bullets with an image
	ppBulletUnnumbered = 1  # Unnumbered bullets


class PpChangeCase:
	ppCaseLower = 2  # Change to lowercase.
	ppCaseSentence = 1  # Change to lowercase.
	ppCaseTitle = 4  # Change to title case.
	ppCaseToggle = 5  # Toggle the casing.
	ppCaseUpper = 3  # Change to uppercase.


class PpChartUnitEffect:
	ppAnimateByCategory = 2  # By category
	ppAnimateByCategoryElements = 4  # By category elements
	ppAnimateBySeries = 1  # By series
	ppAnimateBySeriesElements = 3  # By series elements
	ppAnimateChartAllAtOnce = 5  # Chart all at once
	ppAnimateChartMixed = -2  # Chart mixed


class PpCheckInVersionType:
	ppCheckInMajorVersion = 1  # Major version
	ppCheckInMinorVersion = 0  # Minor version
	ppCheckInOverwriteVersion = 2  # Overwrite current version


class PpColorSchemeIndex:
	ppAccent1 = 6  # Accent1
	ppAccent2 = 7  # Accent2
	ppAccent3 = 8  # Accent3
	ppBackground = 1  # Background
	ppFill = 5  # Fill
	ppForeground = 2  # Foreground
	ppNotSchemeColor = 0  # Not scheme color
	ppSchemeColorMixed = -2  # Mixed scheme color
	ppShadow = 3  # Shadow
	ppTitle = 4  # Title


class PpDateTimeFormat:
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


class PpDirection:
	ppDirectionLeftToRight = 1  # Left-to-right layout
	ppDirectionMixed = -2  # Mixed layout
	ppDirectionRightToLeft = 2  # Right-to-left layout


class PpEntryEffect:
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
	ppEffectMixed = -2  # Mixed
	ppEffectNewsflash = 3850  # Newsflash
	ppEffectNone = 0  # None
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


class PpFarEastLineBreakLevel:
	ppFarEastLineBreakLevelCustom = 3  # Custom level
	ppFarEastLineBreakLevelNormal = 1  # Normal level
	ppFarEastLineBreakLevelStrict = 2  # Strict level


class PpFixedFormatIntent:
	pFixedFormatIntentPrint = 2  # Intent is to print exported file.
	ppFixedFormatIntentScreen = 1  # Intent is to view exported file on screen.


class PpFixedFormatType:
	ppFixedFormatTypePDF = 2  # PDF format
	ppFixedFormatTypeXPS = 1  # XPS format


class PpFollowColors:
	ppFollowColorsMixed = -2  # The chart colors follow a mixed format of the slide's color scheme.
	ppFollowColorsNone = 0  # The chart colors do not follow the slide's color scheme.
	ppFollowColorsScheme = 1  # All the colors in the chart follow the slide's color scheme.
	ppFollowColorsTextAndBackground = 2  # Only the text and background follow the slide's color scheme.
	ppFrameColorsBlackTextOnWhite = 5  # Use White text on a Black frame.
	ppFrameColorsBrowserColors = 1  # Use browser colors for the pane and text.
	ppFrameColorsPresentationSchemeAccentColor = 3  # Use the Presentation Scheme Accent color.
	ppFrameColorsPresentationSchemeTextColor = 2  # Use the Presentation Scheme Text Color.
	ppFrameColorsWhiteTextOnBlack = 4  # Use Black text on a White frame.


class PpGuideOrientation:
	ppHorizontalGuide = 1  # Represents a horizontal guide, spanning from the left to right of the slide editing window.
	ppVerticalGuide = 2  # Represents a vertical guide, spanning from top edge to bottom of the slide editing window.


class PpHTMLVersion:
	ppHTMLAutodetect = 4  # Autodetect
	ppHTMLDual = 3  # Dual version
	ppHTMLv3 = 1  # HTML Version 3
	ppHTMLv4 = 2  # HTML Version 4 (Default)


class PpMediaTaskStatus:
	ppMediaTaskStatusNone = 0  # No status
	ppMediaTaskStatusInProgress = 1  # In progress
	ppMediaTaskStatusQueued = 2  # Queued
	ppMediaTaskStatusDone = 3  # Done
	ppMediaTaskStatusFailed = 4  # Failed


class PpMediaType:
	ppMediaTypeMixed = -2  # Mixed
	ppMediaTypeMovie = 3  # Movie
	ppMediaTypeOther = 1  # Others
	ppMediaTypeSound = 2  # Sound


class PpMouseActivation:
	ppMouseClick = 1  # Mouse click
	ppMouseOver = 2  # Mouse over


class PpNumberedBulletStyle:
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


class PpParagraphAlignment:
	ppAlignCenter = 2  # Center align
	ppAlignDistribute = 5  # Distribute
	ppAlignJustify = 4  # Justify
	ppAlignJustifyLow = 7  # Low justify
	ppAlignLeft = 1  # Left aligned
	ppAlignmentMixed = -2  # Mixed alignment
	ppAlignRight = 3  # Right-aligned
	ppAlignThaiDistribute = 6  # Thai distributed


class PpPasteDataType:
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


class PpPlaceholderType:
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


class PpPlayerState:
	ppPlaying = 0  # Playing
	ppPaused = 1  # Paused
	ppStopped = 2  # Stopped
	ppNotReady = 3  # Not ready


class PpPrintColorType:
	ppPrintBlackAndWhite = 2  # Black and White
	ppPrintColor = 1  # Colored
	ppPrintPureBlackAndWhite = 3  # Pure Black and White


class PpPrintHandoutOrder:
	ppPrintHandoutHorizontalFirst = 2  # Slides are ordered horizontally, with the first slide in the upper-left corner and the second slide to the right of it. If your language setting specifies a right-to-left language, the first slide is in the upper-right corner with the second slide to the left of it.
	ppPrintHandoutVerticalFirst = 1  # Slides are ordered vertically, with the first slide in the upper-left corner and the second slide below it. If your language setting specifies a right-to-left language, the first slide is in the upper-right corner with the second slide below it.


class PpPrintOutputType:
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


class PpPrintRangeType:
	ppPrintAll = 1  # Print all slides in the presentation.
	ppPrintCurrent = 3  # Print the current slide from the presentation.
	ppPrintNamedSlideShow = 5  # Print a named slideshow.
	ppPrintSelection = 2  # Print a selection of slides.
	ppPrintSlideRange = 4  # Print a range of slides.


class PpProtectedViewCloseReason:
	ppProtectedViewCloseNormal = 0  # Protected view is being closed normally.
	ppProtectedViewCloseEdit = 1  # Protected view is being closed so that the presentation can be edited.
	ppProtectedViewCloseForced = 2  # Protected view is forced closed.


class PpPublishSourceType:
	ppPublishAll = 1  # Publish all.
	ppPublishNamedSlideShow = 3  # Publish a named slideshow.
	ppPublishSlideRange = 2  # Publish a range of slides.


class PpRemoveDocInfoType:
	ppRDIAll = 99  # Remove all document information.
	ppRDIAtMentions = 18  # Remove resolved @mentioned users from comments.
	ppRDIComments = 1  # Remove comments.
	ppRDIContentType = 16  # Remove content type information.
	ppRDIDocumentManagementPolicy = 15  # Remove document management policy information.
	ppRDIDocumentProperties = 8  # Remove document properties.
	ppRDIDocumentServerProperties = 14  # Remove document server properties.
	ppRDIDocumentWorkspace = 10  # Remove document workspace information.
	ppRDIInkAnnotations = 11  # Remove Ink annotations. NOTE: This constant has been deprecated, but it remains part of the object model for backward compatibility. You should not use it in new applications.
	ppRDIPublishPath = 13  # Remove publication path information.
	ppRDIRemovePersonalInformation = 4  # Remove personal information.
	ppRDISlideUpdateInformation = 17  # Remove slide update information.


class PpResampleMediaProfile:
	ppResampleMediaProfileCustom = 1  # Custom profile
	ppResampleMediaProfileSmall = 2  # Small profile
	ppResampleMediaProfileSmaller = 3  # Smaller profile
	ppResampleMediaProfileSmallest = 4  # Smallest profile


class PpRevisionInfo:
	ppRevisionInfoBaseline = 1  # Information baseline.
	ppRevisionInfoMerged = 2  # Information merged.
	ppRevisionInfoNone = 0  # No information.


class PpSaveAsFileType:
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


class PpSelectionType:
	ppSelectionNone = 0  # None
	ppSelectionShapes = 2  # Shapes
	ppSelectionSlides = 1  # Slides
	ppSelectionText = 3  # Text


class PpSlideLayout:
	ppLayoutBlank = 12  # Blank
	ppLayoutChart = 8  # Chart
	ppLayoutChartAndText = 6  # Chart and text
	ppLayoutClipArtAndText = 10  # ClipArt and text
	ppLayoutClipArtAndVerticalText = 26  # ClipArt and vertical text
	ppLayoutComparison = 34  # Comparison
	ppLayoutContentWithCaption = 35  # Content with caption
	ppLayoutCustom = 32  # Custom
	ppLayoutFourObjects = 24  # Four objects
	ppLayoutLargeObject = 15  # Large object
	ppLayoutMediaClipAndText = 18  # MediaClip and text
	ppLayoutMixed = -2  # Mixed
	ppLayoutObject = 16  # Object
	ppLayoutObjectAndText = 14  # Object and text
	ppLayoutObjectAndTwoObjects = 30  # Object and two objects
	ppLayoutObjectOverText = 19  # Object over text
	ppLayoutOrgchart = 7  # Organization chart
	ppLayoutPictureWithCaption = 36  # Picture with caption
	ppLayoutSectionHeader = 33  # Section header
	ppLayoutTable = 4  # Table
	ppLayoutText = 2  # Text
	ppLayoutTextAndChart = 5  # Text and chart
	ppLayoutTextAndClipArt = 9  # Text and ClipArt
	ppLayoutTextAndMediaClip = 17  # Text and MediaClip
	ppLayoutTextAndObject = 13  # Text and object
	ppLayoutTextAndTwoObjects = 21  # Text and two objects
	ppLayoutTextOverObject = 20  # Text over object
	ppLayoutTitle = 1  # Title
	ppLayoutTitleOnly = 11  # Title only
	ppLayoutTwoColumnText = 3  # Two-column text
	ppLayoutTwoObjects = 29  # Two objects
	ppLayoutTwoObjectsAndObject = 31  # Two objects and object
	ppLayoutTwoObjectsAndText = 22  # Two objects and text
	ppLayoutTwoObjectsOverText = 23  # Two objects over text
	ppLayoutVerticalText = 25  # Vertical text
	ppLayoutVerticalTitleAndText = 27  # Vertical title and text
	ppLayoutVerticalTitleAndTextOverChart = 28  # Vertical title and text over chart


class PpSlideShowAdvanceMode:
	ppSlideShowManualAdvance = 1  # Manual Advance
	ppSlideShowRehearseNewTimings = 3  # Rehearsed timings
	ppSlideShowUseSlideTimings = 2  # Specified timings for each slide


class PpSlideShowPointerType:
	ppSlideShowPointerAlwaysHidden = 3  # Pointer is always hidden.
	ppSlideShowPointerArrow = 1  # Arrow pointer used.
	ppSlideShowPointerAutoArrow = 4  # AutoArrow pointer used.
	ppSlideShowPointerEraser = 5  # Eraser pointer used.
	ppSlideShowPointerNone = 0  # No pointer used.
	ppSlideShowPointerPen = 2  # Pen pointer used.


class PpSlideShowRangeType:
	ppShowAll = 1  # Show all.
	ppShowNamedSlideShow = 3  # Show named slideshow.
	ppShowSlideRange = 2  # Show slide range.


class PpSlideShowState:
	ppSlideShowBlackScreen = 3  # Black screen
	ppSlideShowDone = 5  # Done
	ppSlideShowPaused = 2  # Paused
	ppSlideShowRunning = 1  # Running
	ppSlideShowWhiteScreen = 4  # White screen


class PpSlideShowType:
	ppShowTypeKiosk = 3  # Kiosk
	ppShowTypeSpeaker = 1  # Speaker
	ppShowTypeWindow = 2  # Window


class PpSlideSizeType:
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


class PpSoundEffectType:
	ppSoundEffectsMixed = -2  # Mixed
	ppSoundFile = 2  # File
	ppSoundNone = 0  # None
	ppSoundStopPrevious = 1  # Stop Previous


class PpSoundFormatType:
	ppSoundFormatCDAudio = 3  # CD Audio format
	ppSoundFormatMIDI = 2  # MIDI format
	ppSoundFormatMixed = -2  # Mixed format
	ppSoundFormatNone = 0  # No format
	ppSoundFormatWAV = 1  # WAV format


class PpTabStopType:
	ppTabStopCenter = 2  # Center tab stop
	ppTabStopDecimal = 4  # Decimal tab stop
	ppTabStopLeft = 1  # Left tab stop
	ppTabStopMixed = -2  # Mixed
	ppTabStopRight = 3  # Right tab stop


class PpTextLevelEffect:
	ppAnimateByAllLevels = 16  # By all levels
	ppAnimateByFifthLevel = 5  # By fifth level
	ppAnimateByFirstLevel = 1  # By first level
	ppAnimateByFourthLevel = 4  # By fourth level
	ppAnimateBySecondLevel = 2  # By second level
	ppAnimateByThirdLevel = 3  # By third level
	ppAnimateLevelMixed = -2  # Mixed level
	ppAnimateLevelNone = 0  # No level


class PpTextStyleType:
	ppBodyStyle = 3  # Body style
	ppDefaultStyle = 1  # Default style
	ppTitleStyle = 2  # Title style


class PpTextUnitEffect:
	ppAnimateByCharacter = 2  # Text-unit effects are animated by character.
	ppAnimateByParagraph = 0  # Text-unit effects are animated by paragraph.
	ppAnimateByWord = 1  # Text-unit effects are animated by word.
	ppAnimateUnitMixed = -2  # Text-unit effects are animated in a mixed manner.


class PpTransitionSpeed:
	ppTransitionSpeedFast = 3  # Fast
	ppTransitionSpeedMedium = 2  # Medium
	ppTransitionSpeedMixed = -2  # Mixed
	ppTransitionSpeedSlow = 1  # Slow


class PpUpdateOption:
	ppUpdateOptionAutomatic = 2  # Link will be updated each time the presentation is opened or the source file changes.
	ppUpdateOptionManual = 1  # Link will be updated only when the user specifically asks to update the presentation.
	ppUpdateOptionMixed = -2  # Mixed


class PpViewType:
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


class PpWindowState:
	ppWindowMaximized = 3  # Maximized
	ppWindowMinimized = 2  # Minimized
	ppWindowNormal = 1  # Normal


class XlAxisCrosses:
	xlAxisCrossesAutomatic = -4105  # Word sets the axis crossing point.
	xlAxisCrossesCustom = -4114  # The CrossesAt property specifies the axis crossing point.
	xlAxisCrossesMaximum = 2  # The axis crosses at the maximum value.
	xlAxisCrossesMinimum = 4  # The axis crosses at the minimum value.


class XlAxisGroup:
	xlPrimary = 1  # The primary axis group.
	xlSecondary = 2  # The secondary axis group.


class XlAxisType:
	xlCategory = 1  # Axis displays categories.
	xlSeriesAxis = 3  # Axis displays data series.
	xlValue = 2  # Axis displays values.


class XlBackground:
	xlBackgroundAutomatic = -4105  # Word controls the background.
	xlBackgroundOpaque = 3  # An opaque background.
	xlBackgroundTransparent = 2  # A transparent background.


class XlBarShape:
	xlBox = 0  # A box.
	xlConeToMax = 5  # A cone, truncated at the specified value.
	xlConeToPoint = 4  # A cone, coming to a point at the specified value.
	xlCylinder = 3  # A cylinder.
	xlPyramidToMax = 2  # A pyramid, truncated at the specified value.
	xlPyramidToPoint = 1  # A pyramid, coming to a point at the specified value.


class XlBinsType:
	xlBinsTypeAutomatic = 0  # Sets bins type automatically.
	xlBinsTypeCategorical = 1  # Sets bins type by category.
	xlBinsTypeManual = 2  # Sets bins type manually.
	xlBinsTypeBinSize = 3  # Sets bins type by size.
	xlBinsTypeBinCount = 4  # Sets bins type by count.


class XlBorderWeight:
	xlHairline = 1  # A hairline border (thinnest border).
	xlMedium = -4138  # A medium border.
	xlThick = 4  # A thick border (widest border).
	xlThin = 2  # A thin border.


class XlCategoryLabelLevel:
	xlCategoryLabelLevelAll = -1  # Use all category label levels within range on the chart. The default.
	xlCategoryLabelLevelCustom = -2  # Indicates literal data in the category labels.
	xlCategoryLabelLevelNone = -3  # Use no category labels in the chart. Defaults to automatic indexed labels.


class XlCategoryType:
	xlAutomaticScale = -4105  # Word controls the axis type.
	xlCategoryScale = 2  # Axis groups data by an arbitrary set of categories.
	xlTimeScale = 3  # Axis groups data on a time scale.


class XlChartElementPosition:
	xlChartElementPositionAutomatic = -4105  # Automatically sets the position of the chart element.
	xlChartElementPositionCustom = -4114  # Specifies a specific position for the chart element.


class XlChartGallery:
	xlAnyGallery = 23  # Either of the galleries.
	xlBuiltIn = 21  # The built-in gallery.
	xlUserDefined = 22  # The user-defined gallery.


class XlChartItem:
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


class XlChartPicturePlacement:
	xlAllFaces = 7  # Display on all faces.
	xlEnd = 2  # Display on end.
	xlEndSides = 3  # Display on end and sides.
	xlFront = 4  # Display on front.
	xlFrontEnd = 6  # Display on front and end.
	xlFrontSides = 5  # Display on front and sides.
	xlSides = 1  # Display on sides.


class XlChartPictureType:
	xlStack = 2  # The picture is sized to repeat a maximum of 15 times in the longest stacked bar.
	xlStackScale = 3  # The picture is sized to a specified number of units and repeated the length of the bar.
	xlStretch = 1  # The picture is stretched the full length of the stacked bar.


class XlChartSplitType:
	xlSplitByCustomSplit = 4  # The second chart displays arbitrary slides.
	xlSplitByPercentValue = 3  # The second chart displays values less than a percentage of the total value. The percentage is specified by the SplitValue property.
	xlSplitByPosition = 1  # The second chart displays the smallest values in the data series. The number of values to display is specified by the SplitValue property.
	xlSplitByValue = 2  # The second chart displays values less than the value specified by the SplitValue property.


class XlColorIndex:
	xlColorIndexAutomatic = -4105  # Automatic color.
	xlColorIndexNone = -4142  # No color.


class XlConstants:
	xl3DBar = -4099  # Three-dimensional bar chart group or series.
	xl3DSurface = -4103  # Three-dimensional surface chart group or series.
	xlAbove = 0  # The summary row is displayed above the specified range.
	xlAutomatic = -4105  # Word applies automatic settings, such as a color or page number, to the specified object.
	xlBar = 2  # Two-dimensional bar chart group or series.
	xlBelow = 1  # The summary row is displayed below the specified range.
	xlBoth = 1  # Display positive and negative error bars in the specified chart group or series.
	xlBottom = -4107  # Bottom.
	xlCenter = -4108  # Center.
	xlChecker = 9  # Checker pattern.
	xlCircle = 8  # Circle.
	xlColumn = 3  # Columnar chart group or series.
	xlCombination = -4111  # Combination.
	xlCorner = 2  # Corner.
	xlCrissCross = 16  # Criss-cross pattern.
	xlCross = 4  # Cross pattern.
	xlCustom = -4114  # Word applies custom settings, such as a color or error amount, to the specified object.
	xlDefaultAutoFormat = -1  # Word applies default or automatic formatting.
	xlDiamond = 2  # Diamond pattern.
	xlDistributed = -4117  # Distributed.
	xlFill = 5  # Fill.
	xlFixedValue = 1  # Display error amounts as a fixed value.
	xlGeneral = 1  # General.
	xlGray16 = 17  # 16% gray pattern.
	xlGray25 = -4124  # 25% gray pattern.
	xlGray50 = -4125  # 50% gray pattern.
	xlGray75 = -4126  # 75% gray pattern.
	xlGray8 = 18  # 8% gray pattern.
	xlGrid = 15  # Grid pattern.
	xlHigh = -4127  # High.
	xlInside = 2  # Inside.
	xlJustify = -4130  # Justify.
	xlLeft = -4131  # Left.
	xlLightDown = 13  # Light down line pattern.
	xlLightHorizontal = 11  # Light horizontal line pattern.
	xlLightUp = 14  # Light up line pattern.
	xlLightVertical = 12  # Light vertical line pattern.
	xlLow = -4134  # Low.
	xlMaximum = 2  # Maximum.
	xlMinimum = 4  # Minimum.
	xlMinusValues = 3  # Minus values.
	xlNextToAxis = 4  # Next to axis.
	xlNone = -4142  # Do not display error bars in the specified chart group or series.
	xlOpaque = 3  # Opaque fill.
	xlOutside = 3  # Outside.
	xlPercent = 2  # Display error amounts as a percentage.
	xlPlus = 9  # Display positive error bars in the specified chart group or series.
	xlPlusValues = 2  # Plus values.
	xlRight = -4152  # Right.
	xlScale = 3  # Scale.
	xlSemiGray75 = 10  # 75% semi-gray pattern.
	xlShowLabel = 4  # Show label.
	xlShowLabelAndPercent = 5  # Show label and percent.
	xlShowPercent = 3  # Show percent.
	xlShowValue = 2  # Show value.
	xlSingle = 2  # Single line.
	xlSolid = 1  # Solid pattern.
	xlSquare = 1  # Square.
	xlStar = 5  # Star.
	xlStError = 4  # Display error amounts as a standard error.
	xlTop = -4160  # Top.
	xlTransparent = 2  # Transparent fill.
	xlTriangle = 3  # Triangle.


class XlCopyPictureFormat:
	xlBitmap = 2  # A bitmap (.bmp, .jpg, .gif).
	xlPicture = -4147  # A drawn picture (.png, .wmf, .mix).


class XlDataLabelPosition:
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


class XlDataLabelSeparator:
	xlDataLabelSeparatorDefault = 1  # Word selects the separator.


class XlDataLabelsType:
	xlDataLabelsShowBubbleSizes = 6  # Show the size of the bubble in reference to the absolute value.
	xlDataLabelsShowLabel = 4  # The category for the point.
	xlDataLabelsShowLabelAndPercent = 5  # The percentage of the total, and the category for the point. Available only for pie charts and doughnut charts.
	xlDataLabelsShowNone = -4142  # No data labels.
	xlDataLabelsShowPercent = 3  # The percentage of the total. Available only for pie charts and doughnut charts.
	xlDataLabelsShowValue = 2  # The default value for the point (assumed if this argument is not specified).


class XlDisplayBlanksAs:
	xlInterpolated = 3  # Values are interpolated into the chart.
	xlNotPlotted = 1  # Blank cells are not plotted.
	xlZero = 2  # Blanks are plotted as zero.


class XlDisplayUnit:
	xlHundredMillions = -8  # Hundreds of millions.
	xlHundreds = -2  # Hundreds.
	xlHundredThousands = -5  # Hundreds of thousands.
	xlMillionMillions = -10  # Millions of millions.
	xlMillions = -6  # Millions.
	xlTenMillions = -7  # Tens of millions.
	xlTenThousands = -4  # Tens of thousands.
	xlThousandMillions = -9  # Thousands of millions.
	xlThousands = -3  # Thousands.


class XlEndStyleCap:
	xlCap = 1  # Caps are applied.
	xlNoCap = 2  # No caps are applied.

class XlErrorBarDirection:
	xlChartX = -4168  # Bars run parallel to the y-axis for x-axis values.
	xlChartY = 1  # Bars run parallel to the x-axis for y-axis values.


class XlErrorBarInclude:
	xlErrorBarIncludeBoth = 1  # Both the positive and negative error range.
	xlErrorBarIncludeMinusValues = 3  # Only the negative error range.
	xlErrorBarIncludeNone = -4142  # No error bar range.
	xlErrorBarIncludePlusValues = 2  # Only the positive error range.


class XlErrorBarType:
	xlErrorBarTypeCustom = -4114  # The range is set by fixed values or cell values.
	xlErrorBarTypeFixedValue = 1  # Fixed-length error bars.
	xlErrorBarTypePercent = 2  # The percentage of the range to be covered by the error bars.
	xlErrorBarTypeStDev = -4155  # Shows the range for a specified number of standard deviations.
	xlErrorBarTypeStError = 4  # Shows the standard error range.


class XlHAlign:
	xlHAlignCenter = -4108  # Center.
	xlHAlignCenterAcrossSelection = 7  # Center across selection.
	xlHAlignDistributed = -4117  # Distribute.
	xlHAlignFill = 5  # Fill.
	xlHAlignGeneral = 1  # Align according to data type.
	xlHAlignJustify = -4130  # Justify.
	xlHAlignLeft = -4131  # Left.
	xlHAlignRight = -4152  # Right.


class XlLegendPosition:
	xlLegendPositionBottom = -4107  # Below the chart.
	xlLegendPositionCorner = 2  # In the upper-right corner of the chart border.
	xlLegendPositionCustom = -4161  # A custom position.
	xlLegendPositionLeft = -4131  # Left of the chart.
	xlLegendPositionRight = -4152  # Right of the chart.
	xlLegendPositionTop = -4160  # Above the chart.


class XlLineStyle:
	xlContinuous = 1  # A continuous line.
	xlDash = -4115  # A dashed line.
	xlDashDot = 4  # Alternating dashes and dots.
	xlDashDotDot = 5  # A dash followed by two dots.
	xlDot = -4118  # A dotted line.
	xlDouble = -4119  # A double line.
	xlLineStyleNone = -4142  # No line.
	xlSlantDashDot = 13  # Slanted dashes.


class XlMarkerStyle:
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


class XlOrientation:
	xlDownward = -4170  # Text runs downward.
	xlHorizontal = -4128  # Text runs horizontally.
	xlUpward = -4171  # Text runs upward.
	xlVertical = -4166  # Text runs downward and is centered in the cell.


class XlParentDataLabelOptions:
	xlParentDataLabelOptionsNone = 0  # No parent labels are shown.
	xlParentDataLabelOptionsBanner = 1  # The parent label layout is a banner above the category.
	xlParentDataLabelOptionsOverlapping = 2  # The parent label is laid out within the category.


class XlPattern:
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


class XlPictureAppearance:
	xlPrinter = 2  # The picture is copied as it will look when it is printed.
	xlScreen = 1  # The picture is copied to resemble its display on the screen as closely as possible.


class XlPieSliceIndex:
	xlCenterPoint = 5  # The center point of a pie slice.
	xlInnerCenterPoint = 8  # The innermost center point of a doughnut slice.
	xlInnerClockwisePoint = 7  # The innermost point of the most clockwise radius of a doughnut slice.
	xlInnerCounterClockwisePoint = 9  # The innermost point of the most counterclockwise radius of a doughnut slice.
	xlMidClockwiseRadiusPoint = 4  # The midpoint of the most clockwise radius of a slice.
	xlMidCounterClockwiseRadiusPoint = 6  # The midpoint of the most counterclockwise radius of a slice.
	xlOuterCenterPoint = 2  # The outer center point of the circumference of a slice.
	xlOuterClockwisePoint = 3  # The outermost clockwise point of the circumference of a slice.
	xlOuterCounterClockwisePoint = 1  # The outermost counterclockwise point of the circumference of a slice.


class XlPieSliceLocation:
	xlCenterPoint = 5  # The center point of a pie slice.
	xlInnerCenterPoint = 8  # The innermost center point of a doughnut slice.
	xlInnerClockwisePoint = 7  # The innermost point of the most clockwise radius of a doughnut slice.
	xlInnerCounterClockwisePoint = 9  # The innermost point of the most counterclockwise radius of a doughnut slice.
	xlMidClockwiseRadiusPoint = 4  # The midpoint of the most clockwise radius of a slice.
	xlMidCounterClockwiseRadiusPoint = 6  # The midpoint of the most counterclockwise radius of a slice.
	xlOuterCenterPoint = 2  # The outer center point of the circumference of a slice.
	xlOuterClockwisePoint = 3  # The outermost clockwise point of the circumference of a slice.
	xlOuterCounterClockwisePoint = 1  # The outermost counterclockwise point of the circumference of a slice.


class XlPivotFieldOrientation:
	xlColumnField = 2  # A column field.
	xlDataField = 4  # A data field.
	xlHidden = 0  # A hidden field.
	xlPageField = 3  # A page field.
	xlRowField = 1  # A row field.


class XlReadingOrder:
	xlContext = -5002  # According to context.
	xlLTR = -5003  # Left-to-right.
	xlRTL = -5004  # Right-to-left.


class XlRgbColor:
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
	xlDarkGray = 11119017  # Dark Gray
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
	xlDarkSlateGray = 5197615  # Dark Slate Gray
	xlDarkSlateGrey = 5197615  # Dark Slate Grey
	xlDarkTurquoise = 13749760  # Dark Turquoise
	xlDarkViolet = 13828244  # Dark Violet
	xlDeepPink = 9639167  # Deep Pink
	xlDeepSkyBlue = 16760576  # Deep Sky Blue
	xlDimGray = 6908265  # Dim Gray
	xlDimGrey = 6908265  # Dim Grey
	xlDodgerBlue = 16748574  # Dodger Blue
	xlFireBrick = 2237106  # Fire Brick
	xlFloralWhite = 15792895  # Floral White
	xlForestGreen = 2263842  # Forest Green
	xlFuchsia = 16711935  # Fuchsia
	xlGainsboro = 14474460  # Gainsboro
	xlGhostWhite = 16775416  # Ghost White
	xlGold = 55295  # Gold
	xlGoldenrod = 2139610  # Goldenrod
	xlGray = 8421504  # Gray
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
	xlLightCyan = 9145088  # Light Cyan
	xlLightGoldenrodYellow = 13826810  # LightGoldenrodYellow
	xlLightGray = 13882323  # Light Gray
	xlLightGreen = 9498256  # Light Green
	xlLightGrey = 13882323  # Light Grey
	xlLightPink = 12695295  # Light Pink
	xlLightSalmon = 8036607  # Light Salmon
	xlLightSeaGreen = 11186720  # Light Sea Green
	xlLightSkyBlue = 16436871  # Light Sky Blue
	xlLightSlateGray = 10061943  # Light Slate Gray
	xlLightSlateGrey = 10061943  # Light Slate Grey
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
	xlNavyBlue = 8388608  # Navy Blue
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
	xlSlateGray = 9470064  # Slate Gray
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


class XlRowCol:
	xlColumns = 2  # The data series is in a row.
	xlRows = 1  # The data series is in a column.


class XlScaleType:
	xlScaleLinear = -4132  # A linear scale.
	xlScaleLogarithmic = -4133  # A logarithmic scale.


class XlSeriesNameLevel:
	xlSeriesNameLevelAll = -1  # Sets series names to all series name levels within range on the chart. The default.
	xlSeriesNameLevelCustom = -2  # Indicates literal data in the series names.
	xlSeriesNameLevelNone = -3  # Sets no series names in the chart.


class XlSizeRepresents:
	xlSizeIsArea = 1  # The area of the bubble.
	xlSizeIsWidth = 2  # The width of the bubble.


class XlTickLabelOrientation:
	xlTickLabelOrientationAutomatic = -4105  # The text orientation is set by Microsoft Word.
	xlTickLabelOrientationDownward = -4170  # The text runs downward.
	xlTickLabelOrientationHorizontal = -4128  # The characters run horizontally.
	xlTickLabelOrientationUpward = -4171  # The text runs upward.
	xlTickLabelOrientationVertical = -4166  # The characters run vertically.


class XlTickLabelPosition:
	xlTickLabelPositionHigh = -4127  # The top or right side of the chart.
	xlTickLabelPositionLow = -4134  # The bottom or left side of the chart.
	xlTickLabelPositionNextToAxis = 4  # Next to the axis (where the axis is not at either side of the chart).
	xlTickLabelPositionNone = -4142  # No tick marks.


class XlTickMark:
	xlTickMarkCross = 4  # Crosses the axis.
	xlTickMarkInside = 2  # Inside the axis.
	xlTickMarkNone = -4142  # No mark.
	xlTickMarkOutside = 3  # Outside the axis.


class XlTimeUnit:
	xlDays = 0  # Days
	xlMonths = 1  # Months
	xlYears = 2  # Years


class XlTrendlineType:
	xlExponential = 5  # Uses an equation to calculate the least squares fit through points (for example, y=ab^x) .
	xlLinear = -4132  # Uses the linear equation y = mx + b to calculate the least squares fit through points.
	xlLogarithmic = -4133  # Uses the equation y = c ln x + b to calculate the least squares fit through points.
	xlMovingAvg = 6  # Uses a sequence of averages computed from parts of the data series. The number of points equals the total number of points in the series minus the number specified for the period.
	xlPolynomial = 3  # Uses an equation to calculate the least squares fit through points (for example, y = ax^6 + bx^5 + cx^4 + dx^3 + ex^2 + fx + g).
	xlPower = 4  # Uses an equation to calculate the least squares fit through points (for example, y = ax^b).
	xlUnderlineStyleDouble = -4119  # Double thick underline.
	xlUnderlineStyleDoubleAccounting = 5  # Two thin underlines placed close together.
	xlUnderlineStyleNone = -4142  # No underline.
	xlUnderlineStyleSingle = 2  # Single underline.
	xlUnderlineStyleSingleAccounting = 4  # Not supported.


class XlVAlign:
	xlVAlignBottom = -4107  # Bottom alignment.
	xlVAlignCenter = -4108  # Center alignment.
	xlVAlignDistributed = -4117  # Distributed alignment.
	xlVAlignJustify = -4130  # Justified alignment.
	xlVAlignTop = -4160  # Top alignment.