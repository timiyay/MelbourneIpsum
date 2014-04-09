import sublime
import sublime_plugin

from random import random

MELB_WORDS = [
    "mamasita", "ticket inspector", "world's most liveable city", "myki queues", "ball", "formula one grand prix",
    "dumplings", "spiegeltent", "graffiti", "hook turns", "collingwood ferals", "the G'", "the borek woman",
    "secret laneway bars", "bespectacled girls", "hipsters", "frankston bogans", "the espy", "emerald peacock",
    "south of the river", "brunswick and brunswick st", "chaddie", "carlton", "footscray hobos", "swanston", "fed square",
    "flemington racecourse", "melb", "naked for satan", "running the tan", "trams", "essendon bombers", "richmond tigers",
    "spring racing carnival", "moomba", "temper trap", "melbourne central", "swanston", "don dons", "rooftop bars",
    "the emerald peacock", "purple emerald", "hu tong dumplings", "movida", "a macaron connoisseur", "cumulus inc",
    "laksa king", "the corner hotel", "pellegrini's", "rocking out the espy", "cookie", "trams", "prahran hipsters",
    "four seasons in one day", "NGV culture fix", "north of the river", "cold drip coffee", "citylink", "rooftop cinema",
    "footy", "north melbourne shinboners", "victory vs heart", "etihad stadium", "aami park", "the melbourne cup",
    "the australian open", "formula one grand prix", "spring racing carnival", "presets", "empire of the sun",
    "grammar vs scotch", "chopper read", "melbourne cricket ground", "neatly trimmed moustaches", "MSAC",
    "the city loop", "bill clinton ate two bowls", "victoria street dodgies", "melb", "brown alley",
    "east brunswick club", "lions bar", "the croft institute", "richmond tigers", "the hawks", "the saints",
    "the rebels", "the storm", "chapel street", "brunswick st hippy", "dandenong", "bourke st mall", "posh brighton",
    "avalon is so not melb", "tullamarine", "werribee wildlife", "fairy penguins", "collins place", "warehouse chic",
    "spencer st station", "middle-aged lycra clad cyclists", "food bloggers", "the bulldogs", "Rod Laver",
    "lygon street spruikers", "street art", "don't paint over the banksy's", "yarra", "old melbourne gaol", "vic market",
    "south melb dim sims", "burlesque", "ac/dc", "dame edna", "cate blanchette", "geoffrey rush", "kath and kim",
    "the crazy wing challenge", "kylie minogue", "shane warne", "black is alway in fashion"
]


class MelbourneIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        self.melb_words = MELB_WORDS
        self.ipsum      = ""
        cursor_position = self.view.sel()[0].a

        self._generate_ipsum()
        self.view.insert(edit, cursor_position, self.ipsum)

    def _generate_ipsum(self, paragraph_length="long", num_paragraphs=2):

        paragraph_length = 20 if paragraph_length == "long" else 10
        self.ipsum = ""

        for i in range(0, num_paragraphs):

            print("doing the Melbourne shuffle...")
            self._shuffle_words()

            for j in range(0, paragraph_length):
                the_words = self.melb_words[j]

                if (j == 0):
                    self.ipsum += the_words[0].upper()
                    the_words = the_words[1:]

                if j % 5 == 1:
                    self.ipsum += the_words + ", "
                else:
                    self.ipsum += the_words + " "

            self.ipsum = self.ipsum.strip()
            # self.ipsum = self.ipsum + "\n\n" if i < num_paragraphs else self.ipsum
            
            if i < (num_paragraphs - 1):
                print('newlines')
                self.ipsum = self.ipsum + "\n\n"
            

    def _shuffle_words(self):

        num_words = len(self.melb_words)

        for i in range(num_words, 0, -1):
            j, x = int(random() * num_words), self.melb_words[i - 1]
            self.melb_words[i - 1] = self.melb_words[j]
            self.melb_words[j] = x
