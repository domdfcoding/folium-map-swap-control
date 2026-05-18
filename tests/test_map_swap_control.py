# 3rd party
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_folium_tools import set_branca_random_seed
from folium import Map

# this package
from folium_map_swap_control import MapSwapControl


def test_control(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750))
	MapSwapControl(
			maps={
					'<i class="fa-solid fa-fire fa-fw"></i> Heatmap': "heatmap.html",
					'<i class="fa-solid fa-camera fa-fw"></i> Photos': "photos.html",
					'<i class="fa-solid fa-plane fa-fw"></i> Radar': "radar.html",
					},
			).add_to(m)

	root = m.get_root()
	html = root.render()
	advanced_file_regression.check(html, extension=".html")
