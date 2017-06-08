import fresh_tomatoes
import media


atonement = media.Movie("Atonement",
                        "Fledgling writer Briony Tallis, as a 13-year-old, irrevocably changes the course of several lives when she accuses her older sister's lover of a crime he did not commit. Based on the British romance novel by Ian McEwan.",
                        "http://images.fanpop.com/images/image_uploads/Atonement-Poster-atonement-267165_1240_930.jpg",
                        "https://www.youtube.com/watch?v=Dznc_LJIJ4c&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DDznc_LJIJ4c&has_verified=1")


ice_age = media.Movie("Ice Age",
                      "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.",
                      "http://babystreaming.com/wp-content/uploads/2014/01/Ice-Age.jpg",
                      "https://www.youtube.com/watch?v=VsvaFxkXrbg")


skeleton_twins = media.Movie("The Skeleton Twins",
                             "Having both coincidentally cheated death on the same day, estranged twins reunite with the possibility of mending their relationship.",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/the-skeleton-twins-2014/large_large_p0p30eIBXwqHtqqDUqOwXYadL6F.jpg",
                             "https://www.youtube.com/watch?v=nhULZJDXLaE")

bridesmaids = media.Movie("Bridesmaids",
                          "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
                          "http://greenweddingshoes.com/wp-content/uploads/2011/05/bridesmaids-movie-poster.jpg",
                          "https://www.youtube.com/watch?v=FNppLrmdyug")
                          

                          
good_time = media.Movie("For a Good Time Call",
                        "Former college frenemies Lauren and Katie move into a fabulous Gramercy Park apartment, and in order to make ends meet, the unlikely pair start a phone sex line together.",
                        "http://ia.media-imdb.com/images/M/MV5BMjI0MTMyNTQ5NV5BMl5BanBnXkFtZTcwNTgxOTM5Nw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=qigVz5l8v9Q")

hector = media.Movie("Hector and the Search for Happiness",
                     "A psychiatrist searches the globe to find the secret of happiness.",
                     "https://3.bp.blogspot.com/-FaKyHi31sNY/U_iIEhLhLkI/AAAAAAAAACY/xauGwuU84SI/s1600/Hector+and+the+Search+for+Happiness+New+Smiley+Poster.jpg",
                     "https://www.youtube.com/watch?v=iWFVAIbIkS4")


movies = [atonement, ice_age, skeleton_twins, bridesmaids, good_time, hector]
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)
