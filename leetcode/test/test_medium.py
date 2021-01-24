from ..medium import numIslands


def test_num_islands():

    assert numIslands(grid=[["1"]]) == 1
    assert numIslands(grid=[[]]) == 0
    assert (
        numIslands(
            grid=[
                ["0", "0", "0", "0"],
                ["0", "0", "0", "0"],
            ]
        )
        == 0
    )
    assert (
        numIslands(
            grid=[
                ["0", "1", "1", "0", "1", "0"],
                ["0", "1", "1", "0", "1", "0"],
                ["0", "1", "1", "0", "1", "1"],
                ["0", "0", "0", "0", "0", "1"],
                ["0", "1", "1", "0", "1", "1"],
            ]
        )
        == 3
    )
