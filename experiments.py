import logging
import time

from auctions import GnuthPlayerSpecification, FirstPriceAuction, PezanisAuction, AuctionPlayerSpecification


def do_pezanis_experiments():
    player_valuations = range(0, 3)
    opponent_valuations = range(-6, 3)

    # player_valuations = range(0, 11)
    # opponent_valuations = range(-30, 11)

    game_name = "pezanis_" + str(len(player_valuations)) + "_strong_" + str(len(opponent_valuations)) + "_weak_auction"

    start_time = time.time()
    sample_auction = PezanisAuction(game_name=game_name, player_valuations=player_valuations,
                                    opponent_valuations=opponent_valuations,
                                    no_jumps=True)

    sample_auction.calculate_equilibria()
    logging.info("--- %s seconds ---" % (time.time() - start_time))


def do_allpay_experiments():
    # player_valuations = range(0, 3)
    # player_valuations = range(0, 6)

    player_valuations = range(0, 7)

    start_time = time.time()

    for no_jumps in [True, False]:
        for no_ties in [False, True]:
            run_allpay(player_valuations, no_jumps, no_ties)

    logging.info("--- %s seconds ---" % (time.time() - start_time))


def run_allpay(player_valuations, no_jumps, no_ties):
    game_name = "allpay_noties_" + str(no_ties) + "_nojumps_" + str(no_jumps) + "_" + str(
        len(player_valuations)) + "_valuations_auction"

    player_specification = AuctionPlayerSpecification(player_actions=player_valuations, player_types=player_valuations,
                                                      no_jumps=no_jumps)
    opponent_specification = AuctionPlayerSpecification(player_actions=player_valuations,
                                                        player_types=player_valuations, no_jumps=no_jumps)

    another_sample_auction = FirstPriceAuction(game_name=game_name,
                                               player_specification=player_specification,
                                               opponent_specification=opponent_specification, all_pay=True,
                                               no_ties=no_ties)

    logging.info("Running: " + game_name)
    another_sample_auction.calculate_equilibria()


def do_gnuth_experiments():
    # player_valuations = range(50, 53)
    # opponent_valuations = range(50, 52)

    player_valuations = range(50, 56)
    opponent_valuations = range(50, 54)
    #
    # player_valuations = range(50, 59)
    # opponent_valuations = range(50, 56)
    #
    # player_valuations = range(50, 62)
    # opponent_valuations = range(50, 58)

    # player_valuations = range(50, 65)
    # opponent_valuations = range(50, 60)

    # player_valuations = range(50, 200 + 1)
    # opponent_valuations = range(50, 150 + 1)

    game_name = str(len(player_valuations)) + "_strong_" + str(len(opponent_valuations)) + "_weak_auction"

    start_time = time.time()
    player_specification = GnuthPlayerSpecification(player_valuations=player_valuations)
    opponent_specification = GnuthPlayerSpecification(player_valuations=opponent_valuations)

    sample_auction = FirstPriceAuction(game_name=game_name, player_specification=player_specification,
                                       opponent_specification=opponent_specification)

    sample_auction.calculate_equilibria()
    logging.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    do_allpay_experiments()
