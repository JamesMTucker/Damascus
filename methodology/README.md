# Digital Scholarly Editions of the Dead Sea Scrolls and Cairo Genizah

# Palaeography (Palaeographic Notebooks)

____

The following is the data model created by James M. Tucker.
____
## Description

While it is feasible to create a web based front-end to facilitate the process of transcription, it is equally possible to use existing software, as is the case here. The reason we use existing software is because there is currently no workspace available to accomplish our work. Thus, the excel notebook is used for three reasons:

1. The cost to engineer a web-based front-end is not trivial;
2. There is currently no possible way to accomplish this work within the Scripta Qumranica workspace (so-called VRE);
3. The Excel file ensures data accuracy at several levels, thus enforcing best philological practices; and
4. Processing data in an Excel format is extensively supported in languages such as Perl, Python, Swift, and JavaScript.

The following palaeographical model facilitates a careful analysis of ancient fragments, either lapidary and/or non-lapidary and in whatever language.
<!--
## Images of an Artefact

## Annotation of Signs

To accumulate a database of signs, it is necessary to first begin by annotating an image with regions of interest. Let's first analyse what is meant by signs. A sign is any semantic bearing mark made on an image of a fragment ([Tucker and Porzig, 2018](https://github.com/JamesMTucker/Damascus/blob/main/bibliography/README.md#articles-or-book-chapters)).

-->

## Structure of the Palaeographic Notebook

The notebook is contains three worksheets: `CHARs`, `SIGNs`, `Frags`.
<!--
The rationale to make three worksheets within one notebook is as follows: A digtial edition is fundamentally an "[interpretation of ancient media translated into different media](https://www.academia.edu/37560923/Material_Philology_and_Digital_Editions_Charting_a_Way_Forward)". Thus, any digital edition today is fundamentally built around high-resolution images of ancient artefacts. To begin the process of making an edition, one needs to annotate the image with `regions of interest` (`ROI`s). `ROI`s are of great utility for clearly annotating what one observes, whether it is extant ink, holes made by larvae, or even subfragments on the Israel Antiquities Authority (IAA) images. After an image has been annotated with `region of interests` (= `rois`), one then has to provide a definition of aforedesignated `ROI`s. Once the specifications of the `rois` are made, it is no longer necessary to have the segmentation information in the foreground—yet it must be easily editable. Thus, the `ROI` specifications are placed in the `SIGNs` worksheet, and then the focus shifts to the `CHARs` workheet. In the `CHAR`s worksheet, each ROI—apart from subfragments—is annotated (defined) as to its interpretation. For the final worksheet, `Sub_Frags`, this sheet holds the `ROI`s of any image whereby there are more than one fragment (especially when the PAM images can demonstrate how successive editors made joins throughout the early years of Qumran Research).
-->
Each worksheet is hereby explained in terms of their definitions and datatypes:

### The SIGNs Worksheet

The following fields are located on the `SIGNs` worksheet:

* `roi_id`:
  * datatype = `INT`
  * definition = a segmented portion of a source image (normally in a a linear development of ids for the `rois`, thus rois += 1)

* `iaa_related_to`:
  * datatype = `INT` (id of of your image file, if you are storing your files in a database, otherwise change datatype to `VARCHAR` and use the filename)
  * definition = the source from which the `rois` were annotated/computed

* `pam_related_to`:
  * datatype = `INT` (see datatype above for `iaa_related_to`)
  * definition = see above under `iaa_related_to`

* `label`:
  * datatype = `VARCHAR`
  * definition = file source from which the `rois` were generated. This is automatically generated from Fiji, and reduplicates data from `iaa_related_to` or `pam_related_to`. Depending on further datamunging desires, this is not necessary, but it is preserved nonetheless.

* `Area`:
  * datatype = `INT`
  * definition = the area of the segmented roi

* `Mean`:
  * datatype = `FLOAT`
  * definition = Mean grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Min`:
  * datatype = `INT`
  * definition = Min grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Max`:
  * datatype = `INT`
  * definition = Max of grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BX`:
  * datatype = `INT`
  * definition = x-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BY`:
  * datatype = `INT`
  * definition = y-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Width`:
  * datatype = `INT`
  * definition = width of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Height`:
  * datatype = `INT`
  * definition = height of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Major`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Minor`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Angle`:
  * datatype = `FLOAT`
  * definition = Since the methodology ensures that transformations are always understood as interpretations, the need to regress to the original image is therefore crucial. This, however, complicates digital palaeographical practices. To correct this, this column centers the character to the angle of the dry-line.

* `Circ.`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `AR`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Round`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Solidity`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

### CHARs

The following fields are located on the `CHARs` worksheet:
<!--
* `id`:
  * datatype = `INT`
  * definition = for database purposes, leave blank

* `uni_id`:
  * datatype = `INT`
  * definition = a unique id assigned to every `roi`; again for database purposes so leave it blank
-->
* `roi_id`:
  * datatype = `INT`
  * definition = for [Fiji](https://imagej.nih.gov/ij/docs/guide/146.html) datafile; not necessary if using apart from Fiji

* `editors_sigla_id`:
  * datatype = `INT`
  * definition = All of the Judean Desert fragments have been published. Either create an index of these and use the numerical index id, or simply convert field to `VARCHAR` and use a sigla (e.g., `4Q51_1_b`)

* `word_id`:
  * datatype = `INT`
  * definition = Use the word_id from Accordance/QWB; if desired to link with Accordance in a Python Jupyter Notebook (example coming soon!)

* `he_mach`:
  * datatype = `INT`
  * definition = This is generated from a Machine Learning Algorithm. Leave blank and/or ignore.

* `reading_order`:
  * datatype = `INT`
  * definition = A sequence of numbers to specify the reading order of the chars.

* `reading_order_alt`:
  * datatype = `INT`
  * definition = An alternate sequence of numbers to specify the reading order of the chars.; if more than two, iterate to the nth occasion by simply adding a column.

* `attr`:
  * datatype = `ENUM` (`transformed`, `reinked`, `reinked?`, `retraced`, `retraced?`, `interlinear`, `creased`)
  * definition = This field captures **__palaeographical__** attributes of a character

* `related_to`:
  * datatype = `INT`
  * definition = If a character, e.g., relates to a lacuna or is partially damaged by a larva hole, then link the two ids here (roi_ids); these can be computed and properly related into their associated tables later. Use a standard separator for multiple ids (e.g., 40-41-39, 40,41,39, or 40.41.39) [no need to be consistent, a script can detect the separator]

* `is_joined`:
  * datatype = `BOOLEAN` or `TINYINT`
  * definition = More than one sign makes the char, based on a palaeographical _conclusion_. If so, associate specify it is joined. _N.B.: If a char is joined on the basis on two or more signs, then the reading_order is the same for all chars!_

* `kerning`:
  * datatype = `BOOLEAN` or `TINYINT`
  * definition = Is the char under question kerned with the character adjacent to its writing direction? If so, mark with 1.

* `damaged_sm`:
  * datatype = `ENUM` (`TRUE`, `FALSE`, `RELEVANT_X` [or *_W], `RELEVANT_Y` [or *_H])
  * definition = Is the char under question damaged by either material causes or severe surface wear? If so, tag as `TRUE`. If, however, the width or height of the character is still believed to be relevant for font statistics, then designate which axis is still potentially undamaged. This is a preliminary decision. The font algorithm can run further metrics against the `roi` and include it in the [Font Report](https://jamesmtucker.com). N.B.: The font algorithm is not yet published, but will be made available at the above link in due time.
  * UPDATE: damaged_Schriftenmetric implies that, _with respect to designing a font to reverse engineer large scale textual reconstructions_, any sign whose extant ink traces impair an accurate assessment of the height and width of an idiograph is excused from the allographic set of a character of the same definition.

* `damaged_vis`:
  * datatype = `BOOLEAN` or `TINYINT`
  * definition = damaged_visual implies that, with respect to modelling the scribal hand of scribe x apart from photographic evidence, any sign whose extant ink is imparied by physical conditions, such as ink flaking or damaged parchment, is set in any desired colour of font other than black. Degregadation of such a character is comparatively ascertained through a binarized representation of the character whose pixel values are equal to 255 divided by the average of its allograph.

* `damaged_legacy`:
  * datatype = `ENUM` (`certain`, `probable`, `possible`)
  * definition = damaged_legacy implies that, with respect to modelling a textual reconstruction apart from photographic evidence, the DJD sigla of certain [א...ת = char], probable_letter [char + \u0307], possible_letter [char + \u05af] are applied to an idiograph.

* `Angle`:
  * datatype = `INT`
  * defintion = character on image is not level with respect to the ruled line on column

* `he_human_0`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char. Options are:
    * range of chars: א-ת;
    * ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    * s: scribal mark (describe in commentary);
    * and m: material damage (descirbe in commentary)

* `he_human_1`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char _as a palaeographical viable option_.
    * range of chars: א-ת;
    * ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    * s: scribal mark (describe in commentary);
    * and m: material damage (descirbe in commentary)

* `he_human_3`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char _as palaeographical and lexical options permit_.
    * range of chars: א-ת;
    * ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    * s: scribal mark (describe in commentary);
    * and m: material damage (descirbe in commentary)

* `he_human_4`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char _as palaeographical and lexical options permit_. Options are:
    * range of chars: א-ת;
    * ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    * s: scribal mark (describe in commentary);
    * and m: material damage (descirbe in commentary)

* `line_id`:
  * datatype = `INT`
  * definition = Line number on the fragment itself.

* `line_status_int`:
  * datatype = `ENUM` (`DAMAGED`, `DAMAGED_STILL_READ`, `NOT_DAMAGED`)
  * definition = Designate the status of the beginning, middle, and end of line.

* `line_status_mid`:
  * datatype = `ENUM` (`DAMAGED`, `DAMAGED_STILL_READ`, `NOT_DAMAGED`)
  * definition = Designate the status of the beginning, middle, and end of line.

* `line_status_end`:
  * datatype = `ENUM` (`DAMAGED`, `DAMAGED_STILL_READ`, `NOT_DAMAGED`)
  * definition = Designate the status of the beginning, middle, and end of line.

* `commentary`:
  * datatype = `VARCHAR`
  * definition = If you desire to clarify your decisions on the character level. Commentary for columns, sheets, and scrolls can be found/located elsewhere.

### The Sub_Frags Worksheet

* `frag_id`:
  * datatype = `INT`
  * definition = a segmented portion of a source image which defines a subfragment (normally in a linear development of ids for the `rois`, thus frag+id += 1)

* `label`:
  * datatype = `VARCHAR`
  * definition = file source from which the `rois` were generated. This is automatically generated from Fiji, and reduplicates data from `iaa_related_to` or `pam_related_to`. Depending on further datamunging desires, this is not necessary, but it is preserved nonetheless.

* `Area`:
  * datatype = `INT`
  * definition = the area of the segmented roi

* `Mean`:
  * datatype = `FLOAT`
  * definition = Mean grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Min`:
  * datatype = `INT`
  * definition = Min grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Max`:
  * datatype = `INT`
  * definition = Max of grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BX`:
  * datatype = `INT`
  * definition = x-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BY`:
  * datatype = `INT`
  * definition = y-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Width`:
  * datatype = `INT`
  * definition = width of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Height`:
  * datatype = `INT`
  * definition = height of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Major`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Minor`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Angle`:
  * datatype = `FLOAT`
  * definition = Since the methodology ensures that transformations are always understood as interpretations, the need to regress to the original image is therefore crucial. This, however, complicates digital palaeographical practices. To correct this, this column centers the character to the angle of the dry-line.

* `Circ.`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `AR`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Round`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Solidity`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.