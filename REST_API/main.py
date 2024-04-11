# Rest API intermediate(HackerRank)
from urllib.parse import urlencode

import requests


def getWinnerTeam(competition, year):
    """
    Finds the winner of a specified football competition for a given year.

    Args:
        competition (str): The name of the football competition.
        year (int): The year of the competition.

    Returns:
        str: The name of the winning team.
        None: If no winner is found or an error occurs.
    """

    api_url = "https://jsonmock.hackerrank.com/api/football_competitions"
    params = {"name": competition, "year": year}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()["data"]
        return data[0]["winner"] if data else None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def getWinnerTotalGoals(competition, year):
    """
    Determines the winner of a competition and calculates their total goals scored.

    Args:
        competition (str): The name of the football competition.
        year (int): The year of the competition.

    Prints:
        The name of the winning team and their total goals.
    """

    winner_team = getWinnerTeam(competition, year)
    if winner_team:
        total_goals = get_team_total_goals(competition, year, winner_team)
        print(f"Winner: {winner_team}\nTotal Goals: {total_goals}")
    else:
        print("Could not determine winner")


def get_team_total_goals(competition, year, team):
    """
    Calculates the total goals scored by a team in a competition during a given year.

    Args:
        competition (str): The name of the football competition.
        year (int): The year of the competition.
        team (str): The name of the team.

    Returns:
        int: The total number of goals scored by the team.
        None: If no data is found or an error occurs.
    """

    api_url = "https://jsonmock.hackerrank.com/api/football_matches"
    total_goals = 0
    page = 1
    while True:
        params = {"competition": competition, "year": year, "team1": team, "page": page}
        try:
            encoded_params = urlencode(params)
            full_url = f"{api_url}?{encoded_params}"
            response = requests.get(full_url)
            response.raise_for_status()
            data = response.json()
            for match in data["data"]:
                total_goals += (
                    int(match["team1goals"])
                    if match["team1"] == team
                    else int(match["team2goals"]) if match["team2"] == team else 0
                )
            if data["total_pages"] == page:
                break
            else:
                page += 1
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None
    return total_goals


if __name__ == "__main__":
    getWinnerTotalGoals("English Premier League", 2014)
