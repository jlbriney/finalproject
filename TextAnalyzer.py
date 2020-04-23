# Analyze Text with a TextAnalyzer object!

# Your name: Jordan Briney
# Your student id: 77870192
# Your email: jlbriney@umich.edu
# List who you have worked with on this project: Matt powers, Katie wholberg

# import the library needed for testing
import unittest
# you can use the csv library to help you if you wish
import csv
import os


class TextAnalyzer:

    def __init__(self, filepath):
        """Initializes the TextAnalyzer object, using the file at filepath.
        Initialize the following instance variables: filepath (string),
        lines (list)"""
        self.filepath = filepath
        file_info = open(self.filepath, "r")
        self.lines = file_info.readlines()
        file_info.close()

        

    def line_count(self):
        """Returns the number of lines in the file"""
        return len(self.lines)

    def word_count(self):
        """Returns the number of words in the file. A word is defined as any
        text that is separated by whitespace (spaces, newlines, or tabs).
        followed by punctuation (like ? or !)."""
        
        count = 0
        for line in self.lines:
            space = line.strip()
            words = space.strip(".?!,").split(" ")
            count += len(words) 
        return count



    def vocabulary(self):
        """Returns a list of the unique words in the text, sorted in
        alphabetical order. Capitalization should be ignored, so 'Cat' is the
        same word as 'cat'. The returned words should be all lower-case."""
        unique = []
        punctuation = "?!.,"
        for line in self.lines:
            space = line.strip()
            words = space.split()
            for word in words:
                for x in word:
                    if x in punctuation:
                        word = word.replace(x, '')
                word = word.lower()
                if word not in unique:
                    unique.append(word)
        
        return sorted(unique)

    def frequencies(self):
        """Returns a dictionary of the words in the text and the count of how
        many times they appear. The words are the keys, and the counts are the
        values. All the words should be lower case. The order of the keys
        doesn't matter."""
        dict = {}
        punctuation = "?!.,"
        for line in self.lines:
            space = line.strip()
            words = space.split()
            for word in words:
                for x in word:
                    if x in punctuation:
                        word = word.replace(x, '')
                word = word.lower()
                if word in dict:
                    dict[word] += 1
                else: 
                    dict[word] = 1
        return dict


        

    def frequency_of(self, word):
        """Returns the number of times word appears in the text. Capitalization
        should be ignored, so 'Cat' is the same word as 'cat'."""
        self.word = word
        dict = {}
        punctuation = "?!.,"
        for line in self.lines:
            space = line.strip()
            words = space.split()
            for info in words:
                for x in info:
                    if x in punctuation:
                        info = info.replace(x, '')
                info = info.lower()
                if info in dict:
                    dict[info] += 1
                else: 
                    dict[info] = 1
        if self.word.lower() in dict.keys():
            return dict[word.lower()]
        else:
            return 0
        
        

    def percent_frequencies(self):
        """Returns a dictionary of the words in the text and the frequency of the
        words as a percentage of the text. The words are the keys, and the
        counts are the values. All the words should be lower case. The order
        of the keys doesn't matter."""
        dict = {}
        punctuation = "?!.,"
        for line in self.lines:
            space = line.strip()
            words = space.split()
            for info in words:
                for x in info:
                    if x in punctuation:
                        info = info.replace(x, '')
                info = info.lower()
                if info in dict:
                    dict[info] += 1
                else: 
                    dict[info] = 1
        total = 0
        for val in dict.keys():
            total += dict[val]
        for val in dict.keys():
            dict[val] = (dict[val]) / total
        return dict



        

    def most_common(self, n=1):
        """Returns a list of the most common n words in the text. By default,
        n is 1. The returned words should be sorted by frequency.

        There might be a case where multiple words have the same frequency,
        but you can only return some of them due to the n value. In that case,
        return the ones that come first alphabetically."""
        dict = {}
        punctuation = "?!.,"
        for line in self.lines:
            space = line.strip()
            words = space.split()
            for info in words:
                for x in info:
                    if x in punctuation:
                        info = info.replace(x, '')
                info = info.lower()
                if info in dict:
                    dict[info] += 1
                else: 
                    dict[info] = 1
        list_words = sorted(dict.items(), key = lambda x: (-x[1],x[0]))
        
        wrd_lst = []
        for tup in list_words:
            wrd_lst.append(tup[0])
        return wrd_lst[:n]
        

    def read_sample_csv(self):
        """Reads the sample.csv file and returns the list of fieldnames"""

        f = open("sample.csv")
        read = f.readlines()
        headers = read[0]
        head = headers.split(',')
        new = []
        for x in head:
            new.append(x.strip('\n'))
        f.close()
        return new
        
        
        

    def write_analysis_details(self, csvfile):
        """Writes the details of the textual analysis to the csvfile.
        Refer to sample.csv for an example of how this should look."""
        new_csvfile = os.path.join(os.path.dirname(__file__), csvfile)
        with open(new_csvfile, 'w') as csvfile:
            csv_file = csv.writer(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            csv_file.writerow(["filepath", "total words", "line count", "most common word"])
            csv_file.writerow([self.filepath, self.word_count(), self.line_count(), self.most_common()[0]])
        return csv_file








        

    def similarity_with(self, other_text_analyzer, n):
        """Extra credit. Calculates the similarity between this text and
        the other text using cosine similarity. See project specification
        for details."""
        pass


# These are the tests. The main() is all the way at the bottom.

class TestLineCount(unittest.TestCase):

    def test_line_count_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.line_count(), 1)
        # Check that it works when called a second time
        self.assertEqual(ta.line_count(), 1)

    def test_line_count_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.line_count(), 3)
        # Check that it works when called a second time
        self.assertEqual(ta.line_count(), 3)

    def test_line_count_the_victors(self):
        ta = TextAnalyzer("files_for_testing/the_victors.txt")
        self.assertEqual(ta.line_count(), 33)
        # Check that it works when called a second time
        self.assertEqual(ta.line_count(), 33)


class TestWordCount(unittest.TestCase):

    def test_word_count_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.word_count(), 4)
        # Check that it works when called a second time
        self.assertEqual(ta.word_count(), 4)

    def test_word_count_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.word_count(), 24)
        # Check that it works when called a second time
        self.assertEqual(ta.word_count(), 24)

    def test_word_count_the_victors(self):
        ta = TextAnalyzer("files_for_testing/the_victors.txt")
        self.assertEqual(ta.word_count(), 175)
        # Check that it works when called a second time
        self.assertEqual(ta.word_count(), 175)


class TestFrequencies(unittest.TestCase):

    def test_frequencies_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.frequencies()['coffee'], 1)
        self.assertEqual(ta.frequencies()['is'], 1)
        self.assertEqual(ta.frequencies()['good'], 1)

    def test_frequencies_tiny2(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_2.txt")
        self.assertEqual(ta.frequencies()['you'], 1)
        self.assertEqual(ta.frequencies()['hate'], 1)
        self.assertEqual(ta.frequencies()['tea'], 1)

    def test_frequencies_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.frequencies()['i'], 3)
        self.assertEqual(ta.frequencies()['love'], 2)
        self.assertEqual(ta.frequencies()['coffee'], 1)
        self.assertEqual(ta.frequencies()['so'], 12)
        self.assertEqual(ta.frequencies()['much'], 3)


class TestFrequencyOf(unittest.TestCase):

    def test_frequency_of_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.frequency_of('coffee'), 1)
        self.assertEqual(ta.frequency_of('Coffee'), 1)
        self.assertEqual(ta.frequency_of('is'), 1)
        self.assertEqual(ta.frequency_of('so'), 1)
        self.assertEqual(ta.frequency_of('good'), 1)

    def test_frequency_of_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.frequency_of('i'), 3)
        self.assertEqual(ta.frequency_of('love'), 2)
        self.assertEqual(ta.frequency_of('coffee'), 1)
        self.assertEqual(ta.frequency_of('tea'), 1)
        self.assertEqual(ta.frequency_of('so'), 12)
        self.assertEqual(ta.frequency_of('much'), 3)
        self.assertEqual(ta.frequency_of('juice'), 1)
        self.assertEqual(ta.frequency_of('hate'), 1)

    def test_frequency_of_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.frequency_of('i'), 1)
        self.assertEqual(ta.frequency_of('love'), 1)
        self.assertEqual(ta.frequency_of('coffee'), 1)
        self.assertEqual(ta.frequency_of('so'), 6)
        self.assertEqual(ta.frequency_of('much'), 1)
        self.assertEqual(ta.frequency_of('milk'), 0)


class TestVocabulary(unittest.TestCase):

    def test_vocabulary_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'good', 'is', 'so'])

    def test_vocabulary_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'hate', 'i', 'juice',
                                           'love', 'much', 'so', 'tea'])

    def test_vocabulary_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.vocabulary(), ['coffee', 'i', 'love',
                                           'much', 'so'])


class TestPercentFrequencyOf(unittest.TestCase):

    def test_percent_frequency_of_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertIn('coffee', ta.percent_frequencies())
        self.assertIn('is', ta.percent_frequencies())
        self.assertIn('good', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['is'], 1/4)
        self.assertAlmostEqual(ta.percent_frequencies()['good'], 1/4)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/4)

    def test_percent_frequency_of_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertIn('i', ta.percent_frequencies())
        self.assertIn('love', ta.percent_frequencies())
        self.assertIn('coffee', ta.percent_frequencies())
        self.assertIn('so', ta.percent_frequencies())
        self.assertIn('much', ta.percent_frequencies())
        self.assertIn('hate', ta.percent_frequencies())
        self.assertIn('juice', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 2/24)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['tea'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['juice'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 12/24)
        self.assertAlmostEqual(ta.percent_frequencies()['hate'], 1/24)

    def test_percent_frequency_of_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['coffee'], 1/10)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 6/10)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 1/10)


class TestMostCommon1(unittest.TestCase):

    def test_most_common_1_tiny3(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_3.txt")
        self.assertEqual(ta.most_common(), ['so'])
        self.assertEqual(ta.most_common(2), ['so', 'i'])
        self.assertEqual(ta.most_common(4), ['so', 'i', 'much', 'love'])
        self.assertEqual(ta.most_common(0), [])

    def test_most_common_1_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.most_common(), ['so'])


class TestMostCommonMultipleClearCases(unittest.TestCase):

    def test_most_common_multiple_tiny1(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_1.txt")
        self.assertEqual(ta.most_common(3), ['coffee', 'good', 'is'])

    def test_most_common_multiple_tiny4(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(ta.most_common(5), ['so', 'coffee', 'i',
                                             'love', 'much'])


class TestReadSampleCSV(unittest.TestCase):

    def test_reading_sample_csv(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        self.assertEqual(
            ta.read_sample_csv(),
            ['filepath', 'total words', 'line count', 'most common word']
        )


class TestWriteAnalysis(unittest.TestCase):

    def test_write_analysis_details(self):
        ta = TextAnalyzer("files_for_testing/tinyfile_4.txt")
        ta.write_analysis_details('test.csv')
        f = open('test.csv')
        csv_reader = csv.reader(f, delimiter=',')
        lines = [r for r in csv_reader]
        self.assertEqual(
            lines[0],
            ['filepath', 'total words', 'line count', 'most common word']
        )
        self.assertEqual(
            lines[1],
            ['files_for_testing/tinyfile_4.txt', '10', '1', 'so']
        )
        f.close()


# uncomment the test cases below if you attempt the extra credit
# class TestSimilarity(unittest.TestCase):
#     def test_similarity_when_all_same(self):
#         ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
#         ta2 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 1.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 1.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 1.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 4), 1.0)

#     def test_similarity_when_all_different(self):
#         ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
#         ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 0.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 0.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 0.0)

#     def test_similarity_when_somewhat_different(self):
#         ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
#         ta2 = TextAnalyzer("files_for_testing/tinyfile_3.txt")
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 0.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 0.0)
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 0.0)
#         self.assertAlmostEqual(
#             ta1.similarity_with(ta2, 4),
#             0.4656903154237997
#         )

#     def test_similarity_when_somewhat_different2(self):
#         ta1 = TextAnalyzer("files_for_testing/tinyfile_3.txt")
#         ta2 = TextAnalyzer("files_for_testing/tinyfile_4.txt")
#         self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 1.0)
#         self.assertAlmostEqual(
#             ta1.similarity_with(ta2, 2),
#             0.9569426673946801
#         )
#         self.assertAlmostEqual(
#             ta1.similarity_with(ta2, 3),
#             0.9558988911273408
#         )
#         self.assertAlmostEqual(
#             ta1.similarity_with(ta2, 4),
#             0.9569833408227624
#         )
#         self.assertAlmostEqual(
#             ta1.similarity_with(ta2, 5),
#             0.9910527880706026
#         )


def main():
    # Un-comment this line when you are ready to run the unit tests.
    unittest.main(verbosity=2)

    # You can uncomment out some of these lines to do some simple
    # tests with print statements.
    # Or, use your own print statements here as well!
    fightsong = TextAnalyzer("files_for_testing/fightsong.txt")
    osusong = TextAnalyzer("files_for_testing/osusong.txt")
    # print("Line count is ", fightsong.line_count())
    # print("Word count is ", fightsong.word_count())
    # print("Vocabulary is ", fightsong.vocabulary())
    # print("Frequencies are ", fightsong.frequencies())
    # print("Most common is ", fightsong.most_common())
    # print("Most common 3 are ", fightsong.most_common(3))
    # print("Percent frequencies are ", fightsong.percent_frequencies())
    #
    # ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    # ta2 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    # print(fightsong.similarity_with(osusong, 7))
    #
    # ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    # ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt")
    # print(ta1.similarity_with(ta2, 3))


if __name__ == "__main__":
    main()
