import re

# pattern = r'\\stop'
# sample = r'\stop ping stop '

# pattern = r'\"([\d\.]+)\"'
pattern = r'(?:lat=\")([\d\.]+)'
pattern1 = r'(?:<time>)(?P<datetime>.+)(</time>)'
# pattern = r'My'
# pattern1 = r'(\w\s*)+'
# pattern1 = r'test'
sample = r'My test string. test'
sample1 = r"""<trkseg><trkpt lat="58.8258289173" lon="29.9812439550"><ele>29.46</ele><time>2020-09-17T00:28:36Z</time></trkpt>\
<trkpt lat="58.8258294202" lon="29.9812474754"><ele>29.46</ele><time>2020-09-17T00:28:37Z</time></trkpt>\
<trkpt lat="58.8258320186" lon="29.9812428653"><ele>46.76</ele><time>2020-09-17T00:28:40Z</time></trkpt>\
<trkpt lat="58.8258330245" lon="29.9812428653"><ele>46.76</ele><time>2020-09-17T00:28:41Z</time></trkpt>\
<trkpt lat="58.8258270733" lon="29.9812633172"><ele>46.76</ele><time>2020-09-17T00:29:03Z</time></trkpt>\
<trkpt lat="58.8258120697" lon="29.9812327232"><ele>46.76</ele><time>2020-09-17T00:29:15Z</time></trkpt>\
<trkpt lat="58.8258171827" lon="29.9812258501"><ele>47.24</ele><time>2020-09-17T00:29:54Z</time></trkpt>\
<trkpt lat="58.8258402329" lon="29.9812201504"><ele>47.24</ele><time>2020-09-17T00:30:23Z</time></trkpt>\
<trkpt lat="58.8258383051" lon="29.9812359922"><ele>47.24</ele><time>2020-09-17T00:30:40Z</time></trkpt>\
<trkpt lat="58.8258155901" lon="29.9812008720"><ele>46.76</ele><time>2020-09-17T00:31:07Z</time></trkpt>\
<trkpt lat="58.8258222118" lon="29.9812266044"><ele>47.24</ele><time>2020-09-17T00:31:22Z</time></trkpt>\
<trkpt lat="58.8258435857" lon="29.9812162947"><ele>46.76</ele><time>2020-09-17T00:31:39Z</time></trkpt>\
<trkpt lat="58.8258215412" lon="29.9812176358"><ele>46.76</ele><time>2020-09-17T00:32:00Z</time></trkpt>\
<trkpt lat="58.8258188590" lon="29.9812123552"><ele>47.72</ele><time>2020-09-17T00:32:16Z</time></trkpt>"""

if __name__ == '__main__':
    print(re.search(pattern1, sample))
    # print(re.search(pattern1, sample))
    print(re.findall(pattern1, sample))
    for val in re.finditer(pattern, sample1):
        print(val.group())
    print('+' * 12)
    for val1 in re.finditer(pattern1, sample1):
        print(val1)
        print(val1.groups())
        print(val.group())