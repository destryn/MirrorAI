from MirrorAI.dataset.directional.label_image import label_image
import numpy


def test():
    d = numpy.array([0, 1, 1])
    answer = label_image(d, target=0)
    solution = [1, 0, 0]
    assert (answer == solution).all()
