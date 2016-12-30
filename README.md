# MovieRecon

## Matched/Reconciled Entities

Entities | Field(s) | Dataset(s) | Score Ranking
--- | --- | --- | ---
Agents | **Art Director**, **Copyright Owner**, **Currently stored in**, **DP/Cinematographer**, **Dir Gender**, **Director**, **Distributor**, **Donated By:**, **Editor**, **Inspector's Name**, **Labs used by filmmaker**, **Music**, **Principal Cast**, **Producer**, **Production Company**, **Projectionist's Name**, **Script**, **Stock brand**  | LC, Wikidata | 80%
Form |  **Format type**, **HFA Format(s)**, **HFA Formats**, **Original Format**, *video analog format*, *video definition type* | TBD | TBD
Genre | **Classification**, **Fiction**, **Genre**, **Non Fiction**, **short'**  | TBD | TBD
Language | **Intertitle Language**, **Language**, **Subtitle Language** | TBD | TBD
Place | **Country**, **Currently stored in**, **Setting** | TBD | TBD
Topics | **LOC Authority Subject Headings**, **Pro**, **Subject** | TBD | TBD
Works | **Also known as Title**, **Alternate Title**, **Datecode this print:**, **English Title**, **OCLC #**, **Original Source**, **Original Titles**, **Series title**, **Title on Print**, **Year of Release** | TBD | TBD

## Fields

field/column name | matched? | dataset | notes
--- | --- | --- | ---
'# of cans' | n/a | n/a | ignore, just integer values.
2" core? | n/a | n/a | ignore, either yes or None (boolean as text)
20 fps Time | n/a | n/a | ignore, decimal values.
2007 New Cataloging System? | n/a | n/a | ignore, empty field.
3/4" Video Tapes | n/a | n/a | ignore, just integer values.
AD Strip Level | n/a | n/a | ignore, just integer values, sometimes repeated (weird original data encoding involved).
Accession # | n/a | n/a | ignore, only one value appears.
Accession # OBSOLETE | n/a | n/a | ignore, empty.
additional barcodes | ignore | ignore | empty.
aka Title | ignore | ignore | empty.
**Also known as Title** | WORKS | TBD | why is this separate from the field above? Some bad encoding or typos or bad transliteration involved as well.
**Alternate Title** | WORKS | TBD | Some bad encoding or typos or bad transliteration involved.
Archival Box | ignore | ignore | Yes / No / Empty (boolean as text)
Archival Can | ignore | ignore | Yes / No / Empty (boolean as text)
Archival Core | ignore | ignore | Yes / Ye [typo, presumed] / No / Empty (boolean as text)
Archival Tape Case | ignore | ignore | Yes / No / Empty (boolean as text)
Archivists' choice: | ignore | ignore | string values for sake of viewing recommendation?
**Art Director** | AGENTS, Co-datapoint for WORKS | TBD | First Last format, no other information, not repeated.
Aspect Ratio | ignore | ignore | text values. numeric / text mixing inconsistent for any kind of reuse in datapoint algorithm co-use.
Audience Count | ignore | ignore | empty.
availalbe on: | ignore | ignore | empty.
B/W-Color | ignore | ignore | text values. should be controlled values too inconsistent for any kind of reuse in datapoint algorithm co-use.
bagged & sieved? | ignore | ignore | empty.
Barcode Number | ignore | ignore | some barcodes, sometimes repeated, sometimes text. No value for matching right now.
Barcode Value | ignore | ignore | numbers, worried bad formatting/encoding is making unusable right now regardless (cannot tell if repeated or not).
Base Type: | ignore | ignore | text values. not controlled values it appears.
Best Print Is No. | ignore | ignore | no value for matching, inconsistent text regardless.
Box Quantity | ignore | ignore | integer values.
c_has_lending_records_indicate | ignore | ignore | ignore, either yes or None (boolean as text)
c_has_lending_records_message | ignore | ignore | notes on times lent out.
c_recent_status | ignore | ignore | acquistions status values.
c_searchfield | ignore | ignore | looks like title alternate title director bib identifier fields concatenated. too inconsistent to use for anything here, mostly an indexing process for some discovery system cheat.
Can Sealed? | ignore | ignore | Yes / Empty (boolean as text)
Can Size | ignore | ignore | integer with presumed measurement unit symbol or note. Repeated?
Cautions: | ignore | ignore | text notes.
** Classification** | GENRE | TBD | Genre terms - LCGFT?
*Collection Title* | ignore | ignore | Nothing to match for now. ETDs in future?
Color fade | ignore | ignore | empty.
Condition Defects | ignore | ignore | text notes.
Contact information | ignore | ignore | text notes.
Copyright Info | ignore | ignore | text notes with some kind of code in play.
**Copyright Owner** | AGENT | TBD | More publication statement looking deals than copyrights. text notes, will require more work for matching to Agent URIs. Some just years.
**Country** | PLACE | GEONAMES / WOF | Some are repeated fields. Some countries that no longer exist.
Course No. | ignore | ignore | text notes with some kind of code in play.
**Currently stored in** | PLACE? | TBD | Seems more like repositories, most only make sense within the context of Harvard Libraries. Possible Agent > Organization or Place matching?
**DP/Cinematographer** | AGENT | TBD | Unfortunately, using commas to separate multi-value fields. Looks mostly like First Name Last Name format though.
DRS link location | ignore | ignore | empty
data standardized | ignore | ignore | ignore, either yes or None (boolean as text)
Date Entered | ignore | ignore | date value of a sort (not ISO-compliant)
Date Inspected | ignore | ignore | date value of a sort (not ISO-compliant)
Date Last Edited | ignore | ignore | empty
Date Molecular Sieves | ignore | ignore | date values of a sort (not ISO-compliant)
date moved to current location | ignore | ignore | date values of a sort (not ISO-compliant)
date record last updated | ignore | ignore | date values of a sort (not ISO-compliant)
Date Tested | ignore | ignore | date value of a sort (not ISO-compliant)
Date camphor added | ignore | ignore | empty
Date measured | ignore | ignore | date value of a sort (not ISO-compliant)
Date of Nitrate Inspection | ignore | ignore | empty
Date of arrival at HFA | ignore | ignore | date value of a sort (not ISO-compliant)
Date of record creation | ignore | ignore | date value of a sort (not ISO-compliant)
**Datecode this print:** | WORK co-search datapoint | TBD | Use to match to a Work or some sort of Manifestation? Text note-like values make it really hard to use this though. Generally YYYY [text value], some just no date notes.
**Dir Gender** | AGENT co-search datapoint | TBD | use with Director for matching as needed. Only indicates Female (guess Male/Non-binary is None).
**Director** | AGENT | TBD | Fields repeated, uses commas for separation. First Name Last Name format. Some "none" type notes (vary, beware).
Discs | ignore | ignore | integer
**Distributor** | AGENT | TBD | All Organizations. No repeated fields.
do not access tape until this date unless baked | ignore | ignore | empty.
**Donated By:** | AGENT | TBD | Beware, is more of a note than a name captured.
Dupe Print | ignore | ignore | text note.
Duplicate Print | ignore | ignore | ignore, either yes or None (boolean as text)
*Edited by* | ignore | ignore | empty. Why does this and Editor exist?
**Editor** | AGENT | TBD | some repeated fields with comma or statement of responsibility-type phrase ("in collaboration with").
Element | ignore | ignore | Some kind of technical format value. Varies. Uncertain of value for matching.
Element Copy | ignore | ignore | empty.
**English Title** | WORK co-search datapoint | TBD | few values here, could be helpful, bad formatting/encoding of original data causing problems.
Entered by | ignore | ignore | empty.
Episode # | ignore | ignore | not sure how to use. text note value.
exact date | ignore | ignore | date value of a sort (not ISO-compliant). Not really sure what this exact date is an exact date of.
Excerpt | ignore | ignore | ignore, either yes or None (boolean as text)
FIAF Treasures | ignore | ignore | empty
Features import? | ignore | ignore | ignore, either yes or None (boolean as text)
Feet to Meters | ignore | ignore | integer values.
**Fiction** | GENRE? | TBD | Either FICTION or NON-FICTION. Could match to a genre vocabulary. Field is sometimes repeated (which seems odd).
film in plastic bag? | ignore | ignore | empty.
finding aid online? | ignore | ignore | ignore, either yes or None (boolean as text)
Footage Length | ignore | ignore | inconsistent integer values at length notes.
**Format type** | FORM | TBD | values: Audio, Digital, Film, Paper, Video, film
Frame enlargements made? | ignore | ignore | ignore, either yes or None (boolean as text)
Frame rate | ignore | ignore | integer plus abbreviation for unit of measurement
Gardner standardization | ignore | ignore | ignore, either yes or None (boolean as text)
**Genre** | GENRE | TBD | Further refinement of fields that also somewhat approach Genre above? Can still pull from same external datasets regardless of field scope here. Inconsistent values, some fields repeate, use | not commas
Gift agreement on file? | ignore | ignore | unknown or None.
gSearch | ignore | ignore | empty.
HD shelf ready? | ignore | ignore | empty.
**HFA Format(s)** | FORMAT? | TBD | Format but more specific than FORMs above and definitely not GENRES.
HFA Format(s) Copy | ignore | ignore | empty.
**HFA Formats** | FORMAT? | TBD | Why is this separate from above?
HFA Min to 16mm feet | ignore | ignore | decimal values
HFA Min to 35mm feet | ignore | ignore | decimal values
HFA Number | ignore | ignore | uncertain what this identifier is.
HFA Screening | ignore | ignore | empty.
HFA Screening Date | ignore | ignore | varying date encodings at play. None ISO-compliant forms.
HFA Time | ignore | ignore | varying time or note formats.
HFA Vimeo link | ignore | ignore | empty.
Hard Drive | ignore | ignore | empty.
Has this item been digitized? | ignore | ignore | ignore, either yes or None (boolean as text)
Hollis Record? | ignore | ignore | What is this field? Just seems to have an abstract in it for one record. Or a yes / None boolean type deal.
Hollis updated after discard? | ignore | ignore | empty.
Housed in Original container? | ignore | ignore | ignore, either yes or None (boolean as text) or some kind of note field.
Housed with Original container? | ignore | ignore | ignore, shelf location type field it appears.
Imp | ignore | ignore | note field with some sort of code.
inaccessible until this date unless baked | ignore | ignore | empty.
Ind Piece | ignore | ignore | ignore, either yes or None (boolean as text)
Inspection date | ignore | ignore | date values.
**Inspector's Name** | AGENT? | TBD | Should be matched, but have initials. Unlikely to have matches.
**Intertitle Language** | LANGUAGE | LEXVO | Just English / French.
Intertitles | ignore | ignore | ignore, either Yes / No / or None (boolean as text)
**Item number** | ignore | ignore | Note sure what this identifier applies to. Use for dictionary / json data processing record identifiers though?
Janus update | ignore | ignore | empty
**LOC Authority Subject Headings** | TOPICS | TBD | Subject strings. Typical issues with parsing data from MARC Subject fields.
**Labs used by filmmaker** | AGENT | TBD | Organizations all here.
**Language** | LANGUAGE | LEXVO | some repeated fields, inconsistent manner in which repeated fields are concatenated.
Last Screened at HFA | ignore | ignore | empty
Laurel update | ignore | ignore | ignore, either yes or None (boolean as text)
Leader lady? | ignore | ignore | inconsistently used note field.
location of digitized item | ignore | ignore | ILS identifiers it looks like with some notes.
location of frame enlargement | ignore | ignore | file directories / filepaths.
Metal Film Can | ignore | ignore | empty.
Meters | ignore | ignore | empty.
Meters to Feet | ignore | ignore | empty.
Method of aquisition | ignore | ignore | Gift / Purchase
Method of shipment to HFA | ignore | ignore | note field.
Min to 16mm feet | ignore | ignore | decimal values
Min to 35mm feet | ignore | ignore | integer values.
Mono type | ignore | ignore | note field.
Multiple reels in can? | ignore | ignore | ignore, either yes or None (boolean as text)
**Music** | AGENT | TBD | Will need some pre-match clean up. Fields are repeated. Sometimes just a last name is given.
needs attention? | ignore | ignore | empty.
needs new box? | ignore | ignore | empty.
Needs New Can? | ignore | ignore | ignore, either yes or None (boolean as text)
Needs new Core? | ignore | ignore | ignore, either yes or None (boolean as text)
Needs new HOLLIS update | ignore | ignore | ignore, either yes or None (boolean as text)
Negative Materials | ignore | ignore | empty.
New box design | ignore | ignore | empty.
new print list sent | ignore | ignore | ignore, either yes or None (boolean as text)
Nitrate Decomposition | ignore | ignore | empty.
**Non Fiction** | GENRE? | TBD | Either Non Fiction or None. Could match to a genre vocabulary. Field is sometimes repeated (which seems odd). Why is this different from the FICTION field above?
Notes | ignore | ignore | notes.
Number of Shows | ignore | ignore | empty.
**OCLC #** | WORK co-search datapoint | TBD | Only 4 values. Uncertain of WORK match value at present.
OK for non archival film loan | ignore | ignore | empty.
Obsolete barcode | ignore | ignore | various barcodes. Mostly same pattern.
**Original Format** | FORMAT? | TBD | How differs from FORMAT field usage above? Related manifestation FORMAT?
original inventory box identifier | ignore | ignore | looks like archival shelflist type value, uncertain of use at this point.
Original Production Gauge | ignore | ignore | empty
**Original Source** | WORK? | TBD | Would be a related WORK. Generally field value is FORM: AUTHOR. Could cause lookup problems (inconsistent punctuation, some abbreviations/initials).
Original Title | ignore | ignore | empty.
**Original Titles** | WORK | TBD | usual title inconsistencies in form.
Other | ignore | ignore | empty.
Paperwork | ignore | ignore | note fields.
Paperwork in can? | ignore | ignore | ignore, either yes or None (boolean as text)
Poster | ignore | ignore | empty.
prefix | ignore | ignore | presuming this is for title, not sure which title field it applies to, so ignoring for matching purposes.
preliminary Aleph record | ignore | ignore | empty.
Presently stored on reel? | ignore | ignore | ignore, either yes or Yes or None (boolean as text)
Preservation Statuss | ignore | ignore | few values. Why is this separate from below?
Preservation status | ignore | ignore | note field values.
Preserved by HFA? | ignore | ignore | ignore, either yes or None (boolean as text)
Previously stored with Camphor? | ignore | ignore | empty.
Previously treated? | ignore | ignore | ignore, either yes or Vitafilm or None (boolean as text)
**Principal Cast** | AGENT | TBD | will be a holy mess data format wise for preprocessing to do matching.
Print # | ignore | ignore | note-like values.
Print Condition | ignore | ignore | controlled values, little value to matching.
Print Inspected | ignore | ignore | empty
Print Number | ignore | ignore | empty
**Pro** | TOPIC? | TBD | Not sure what this field is about, looks like a subject-like field though.
Problem with record  for HOLLIS export | ignore | ignore | ignore, either yes or None (boolean as text)
Problem with record  not for HOLLIS export | ignore | ignore | empty.
Problem with record - not for HOLLIS export | ignore | ignore | empty.
processing level | ignore | ignore | controlled values of a sort, not useful for any matching.
**Producer** | AGENT | TBD | Holy terror of data formatting for pre-processing.
**Production Company** | AGENT | TBD | Mostly organizations. Repeated field values. Same formatting issues.
Professor | ignore | ignore | empty.
Professor's Name | ignore | ignore | empty.
Programming Notes | ignore | ignore | note values.
**Projectionist's Name** | AGENT | TBD | Persons, have lots of first initials.
Quality Control | ignore | ignore | empty.
Rare print? | ignore | ignore | ignore, either yes or None (boolean as text)
Recommended as short before feature? | ignore | ignore | ignore, either yes or None (boolean as text)
Recommended for discard | ignore | ignore | ignore, either yes or None (boolean as text)
recommended for preservation | ignore | ignore | yes, note, or other information not relevant for matching.
**record created by** | AGENT | TBD | Worth matching?
Reels | ignore | ignore | integers.
References | ignore | ignore | empty.
Release on file? | ignore | ignore | empty.
Research! | ignore | ignore | ignore, either yes or None (boolean as text)
Running Time {Length} | ignore | ignore | varying time formats / some text note-like given.
SC | ignore | ignore | ignore, either yes or None (boolean as text)
**Script** | AGENT | TBD | watch out for specific roles in parentheses after names. Personal names, some repeated fields separated by commas, names are mostly in format FIRST NAME LAST NAME.
Series | ignore | ignore | ignore, either yes or None (boolean as text)
**Series title** | WORK | TBD | SERIES WORK entity?
**Setting** | PLACE | Geonames & WOF | Countries, States, Cities given.
**short'** | GENRE? | TBD | Another specialized subset of form / genre?
Short Subjects import? | ignore | ignore | ignore, either yes or None (boolean as text)
Shrinkage | ignore | ignore | kind of positive/negative decimal values as percentages given
Sort Running Time | ignore | ignore | hh:mm:ss values given.
Sound Aspect(s) | ignore | ignore | leave for now. Might try to use later for WORK matching.
Soundtrack Type | ignore | ignore | ignore, values don't seem helpful for now.
Special Projection Requirements | ignore | ignore | empty.
Special Topic | ignore | ignore | empty.
Status | ignore | ignore | empty.
Status Report | ignore | ignore | note field.
Stereo Type | ignore | ignore | Code value, uncertain of meaning.
**Stock brand** | Agent | TBD | Organizations.
**Stock type** | ?? | ?? | Seems like something we should be able to match against an external dataset.
Storage Notes | ignore | ignore | note values.
Stored In: | ignore | ignore | seems to repeat purpose of other fields with similar values?
Stored with Camphor? | ignore | ignore | empty.
**Subject** | TOPIC | TBD | repeated values using commas to concatenate
**Subtitle Language** | LANGUAGE | LEXVO | watch for Language & Language concatenation.
Subtitles | ignore | ignore | ignore, either Yes or No or English or None (boolean as text)
Synopsis | ignore | ignore | free text values.
Technical Notes | ignore | ignore | free text values.
**Title on Print** | WORK | TBD | watch out for [none] value.
Tlr | ignore | ignore | ignore, either yes or None (boolean as text)
top button | ignore | ignore | ignore, either yes or None (boolean as text)
Trailers in HFA | ignore | ignore | ignore, either Trailer or None (boolean as text)
Treated for Vinegar Syndrome | ignore | ignore | ignore, either yes or no or None (boolean as text)
treatment description | ignore | ignore | empty.
treatments | ignore | ignore | Could be matched to some external vocabulary, but low priority.
UFSC | ignore | ignore | ignore, either yes or no or None (boolean as text)
US | ignore | ignore | ignore, either yes or None (boolean as text)
unprocessed | ignore | ignore | ignore, either yes or None (boolean as text)
VES Class | ignore | ignore | empty.
VES Course # | ignore | ignore | empty.
VES Professor | ignore | ignore | empty.
Vault Location | ignore | ignore | looks like mostly BIB ids. No use for now.
*video analog format* | ignore? | ignore? | is this another format? Is a another code I'm unsure of.
*video definition type*| ignore? | ignore? | is this another format? Is a another code I'm unsure of.
video inspection results | ignore | ignore | notes
video link location | ignore | ignore | URLs, don't contain any data worth pulling right now.
video smells like | ignore | ignore | note field.
viewed on Cine7D? | ignore | ignore | ignore, either yes or None (boolean as text)
Viewed on Steenbeck? | ignore | ignore | ignore, either yes or None (boolean as text)
Viewed on projector? | ignore | ignore | ignore, either yes or None (boolean as text)
WC | ignore | ignore | integer value, no clue what this is.
**Year of Release** | WORK co-search datapoint | TBD | dates are not formatted consistently. Mostly years. Some qualifiers, mostly abbreviated.
