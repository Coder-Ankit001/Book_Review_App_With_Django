from django.core.management import BaseCommand
from books.models import Book, Genre, Author

BOOKS = [
    ("1984", "George Orwell", ["Dystopian", "Science Fiction"],
     "A totalitarian society under constant surveillance crushes individual freedom, and one man's quiet rebellion against the ruling party leads him toward love, betrayal, and devastating loss."),
    ("Animal Farm", "George Orwell", ["Dystopian", "Satire"],
     "Farm animals overthrow their human owner in pursuit of freedom and equality, only to watch a new tyranny rise from within their own society."),
    ("Pride and Prejudice", "Jane Austen", ["Romance", "Classic Literature"],
     "A sharp-witted young woman navigates family expectations, misplaced pride, and the slow unraveling of prejudice as she falls in love against her better judgment."),
    ("Emma", "Jane Austen", ["Romance", "Classic Literature"],
     "A meddling young woman convinced of her matchmaking skill discovers that love and family happiness are harder to orchestrate than she assumed."),
    ("Sense and Sensibility", "Jane Austen", ["Romance", "Classic Literature"],
     "Two sisters navigate heartbreak, family financial ruin, and the tension between reason and emotion as they each search for love."),
    ("Murder on the Orient Express", "Agatha Christie", ["Mystery", "Crime"],
     "A detective trapped aboard a snowbound train must untangle a web of lies to solve a murder where every passenger seems to have motive."),
    ("And Then There Were None", "Agatha Christie", ["Mystery", "Crime"],
     "Ten strangers lured to an isolated island are killed one by one, forcing the survivors to confront guilt, fear, and the truth behind the murders."),
    ("The Murder of Roger Ackroyd", "Agatha Christie", ["Mystery", "Crime"],
     "A quiet village is shaken by a murder investigation that peels back layers of secrets, deception, and long-buried guilt among its residents."),
    ("The Great Gatsby", "F. Scott Fitzgerald", ["Tragedy", "Classic Literature"],
     "A mysterious millionaire's obsessive love for a woman from his past exposes the hollowness of wealth and the cost of chasing an impossible dream."),
    ("Tender Is the Night", "F. Scott Fitzgerald", ["Tragedy", "Romance"],
     "A promising psychiatrist's marriage and career unravel amid glamorous excess, revealing the fragile line between love and self-destruction."),
    ("War and Peace", "Leo Tolstoy", ["War", "Historical Fiction"],
     "Interwoven families navigate love, loss, and the devastation of war as Napoleon's invasion of Russia reshapes their society and their lives."),
    ("Anna Karenina", "Leo Tolstoy", ["Romance", "Tragedy"],
     "A woman's passionate love affair defies the rigid expectations of her society, leading to devastating consequences for her family and herself."),
    ("Crime and Punishment", "Fyodor Dostoevsky", ["Crime", "Tragedy"],
     "A destitute student's murder of a pawnbroker spirals into a psychological reckoning with guilt, morality, and the possibility of redemption."),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", ["Crime", "Classic Literature"],
     "A family torn apart by rivalry and greed is drawn into a murder investigation that forces each brother to confront faith, guilt, and freedom of conscience."),
    ("Great Expectations", "Charles Dickens", ["Coming-of-Age", "Classic Literature"],
     "An orphan's rise from poverty to gentleman status is shadowed by secrets, misplaced love, and the true cost of ambition."),
    ("A Tale of Two Cities", "Charles Dickens", ["Historical Fiction", "War"],
     "Amid the chaos of the French Revolution, family loyalty and self-sacrificing love are tested against a backdrop of violence and social upheaval."),
    ("Oliver Twist", "Charles Dickens", ["Crime", "Coming-of-Age"],
     "An orphan boy's journey through London's criminal underworld reveals the brutal cost of poverty and the enduring hope for family and belonging."),
    ("To Kill a Mockingbird", "Harper Lee", ["Coming-of-Age", "Historical Fiction"],
     "A small Southern town's deep racial prejudice is exposed through a father's defense of an innocent man, seen through his children's eyes."),
    ("The Hobbit", "J.R.R. Tolkien", ["Fantasy", "Adventure"],
     "A reluctant homebody is swept into a perilous journey across a world of dragons and treasure, discovering unexpected courage along the way."),
    ("The Fellowship of the Ring", "J.R.R. Tolkien", ["Fantasy", "Adventure"],
     "A fragile alliance of unlikely companions sets out on a dangerous journey to destroy a powerful ring before it plunges their world into war."),
    ("A Game of Thrones", "George R.R. Martin", ["Fantasy", "War"],
     "Rival noble families scheme for control of a fractured kingdom, where loyalty, betrayal, and war threaten to tear their society apart."),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", ["Fantasy", "Coming-of-Age"],
     "An orphaned boy discovers he belongs to a hidden magical society and must uncover a dangerous secret threatening his new school and friends."),
    ("Harry Potter and the Chamber of Secrets", "J.K. Rowling", ["Fantasy", "Coming-of-Age"],
     "A young wizard investigates a series of mysterious attacks at his school, uncovering a decades-old secret tied to his own destiny."),
    ("The Old Man and the Sea", "Ernest Hemingway", ["Adventure", "Tragedy"],
     "An aging fisherman's solitary battle against a giant marlin becomes a meditation on endurance, pride, and quiet dignity."),
    ("A Farewell to Arms", "Ernest Hemingway", ["War", "Romance"],
     "A wartime love affair between a soldier and a nurse unfolds against the brutal backdrop of conflict, ending in devastating loss."),
    ("Moby-Dick", "Herman Melville", ["Adventure", "Tragedy"],
     "A sailor's voyage aboard a whaling ship becomes entangled in his captain's obsessive, destructive quest for revenge against a legendary white whale."),
    ("Frankenstein", "Mary Shelley", ["Gothic", "Science Fiction"],
     "A scientist's reckless ambition to conquer death creates a being whose isolation and rejection lead to tragedy for both creator and creation."),
    ("Dracula", "Bram Stoker", ["Gothic", "Horror"],
     "A group of friends band together to hunt down an ancient vampire whose arrival threatens their society with death and corruption."),
    ("Wuthering Heights", "Emily Bronte", ["Gothic", "Tragedy"],
     "An orphan's obsessive, destructive love for his adoptive family's daughter poisons two generations with jealousy, revenge, and loss."),
    ("Jane Eyre", "Charlotte Bronte", ["Gothic", "Romance"],
     "An orphaned governess's quiet resilience and search for love lead her to uncover a dark secret hidden within her employer's household."),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", ["Magical Realism", "Historical Fiction"],
     "A family's generations are shaped by love, war, and repeating cycles of fate in a town where the fantastical and the real intertwine."),
    ("Love in the Time of Cholera", "Gabriel Garcia Marquez", ["Magical Realism", "Romance"],
     "A man's decades-long devotion to his first love survives war, marriage, and the passage of time in a society bound by rigid tradition."),
    ("Brave New World", "Aldous Huxley", ["Dystopian", "Science Fiction"],
     "A society engineered for perfect happiness suppresses individuality and freedom, until one man's doubts threaten to unravel its carefully controlled order."),
    ("Fahrenheit 451", "Ray Bradbury", ["Dystopian", "Science Fiction"],
     "A fireman whose job is burning books begins questioning a society that has traded freedom and thought for shallow, controlled contentment."),
    ("Slaughterhouse-Five", "Kurt Vonnegut", ["War", "Science Fiction"],
     "A soldier who becomes unstuck in time relives the firebombing of Dresden alongside surreal encounters that question the meaning of war and free will."),
    ("The Hunger Games", "Suzanne Collins", ["Dystopian", "Adventure"],
     "A girl volunteers to fight to the death in a televised competition, becoming an unwilling symbol of rebellion against an oppressive society."),
    ("The Kite Runner", "Khaled Hosseini", ["Historical Fiction", "Tragedy"],
     "A childhood betrayal in war-torn Afghanistan haunts a man into adulthood, driving him on a journey toward redemption and family reconciliation."),
    ("A Thousand Splendid Suns", "Khaled Hosseini", ["Historical Fiction", "War"],
     "Two women's lives intertwine amid decades of war and oppression in Afghanistan, bound together by resilience, sacrifice, and hope for freedom."),
    ("The Alchemist", "Paulo Coelho", ["Adventure", "Fantasy"],
     "A shepherd's journey across the desert in pursuit of a recurring dream becomes a search for purpose, love, and his own personal destiny."),
    ("The Road", "Cormac McCarthy", ["Dystopian", "Tragedy"],
     "A father and son journey through a devastated, post-apocalyptic landscape, their bond and quiet hope the only things surviving a ruined society."),
]

class Command(BaseCommand):
    help = "Seeds the database with 40 real books, designed with overlapping authors/genres/plot vocabulary for testing full-text search."

    def handle(self, *args, **kwargs):
        book_count = 0
        for title, author_name, genre_names, plot in BOOKS:

            author, _ = Author.objects.get_or_create(
                name = author_name
            )


            book, book_created = Book.objects.get_or_create(
                title = title,
                author = author,
                defaults = {"plot" : plot}
            )

            genres = []
            for gen in genre_names:
                genre, _ = Genre.objects.get_or_create(
                    name = gen
                )
                genres.append(genre)

            book.genres.set(genres)

            if book_created:
                book_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {title}"))
            else:
                self.stdout.write(f"Already Exists: {title}")

            self.stdout.write(self.style.SUCCESS(f"\n Done {book_count} new books created."))