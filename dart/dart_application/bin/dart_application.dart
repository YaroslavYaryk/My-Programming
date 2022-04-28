import 'dart:collection' show SplayTreeMap;
import 'dart:math' show Point;

/// Returns the y-coordinate for the specified x-coordinate on the line defined
/// by two given points.
double _interpolate(Point<double> p0, Point<double> p1, double x) {
  // y - y0 = m * (x - x0)
  var m = (p1.y - p0.y) / (p1.x - p0.x);
  return m * (x - p0.x) + p0.y;
}

class InterpolatingMap {
  final SplayTreeMap<double, double> _data;

  InterpolatingMap(Map<double, double> data)
      : _data = SplayTreeMap<double, double>.of(data);

  double operator [](double x) {
    var value = _data[x];
    if (value != null) {
      return value;
    }

    if (_data.isEmpty) {
      throw StateError('InterpolatingMap is empty');
    }

    double? lower = _data.lastKeyBefore(x);
    double? upper = _data.firstKeyAfter(x);
    assert(lower != null || upper != null);

    double x0;
    double x1;
    if (lower == null) {
      // `x` is to the left of the left-most data point.  Extrapolate from the
      // first two entries.
      x0 = upper!;
      x1 = _data.firstKeyAfter(upper) ?? x0;
    } else if (upper == null) {
      // `x` is to the right of the right-most data point.  Extrapolate from the
      // last two entries.
      x1 = lower;
      x0 = _data.lastKeyBefore(lower) ?? x1;
    } else {
      x0 = lower;
      x1 = upper;
    }

    return _interpolate(
      Point<double>(x0, _data[x0]!),
      Point<double>(x1, _data[x1]!),
      x,
    );
  }
}

void main() {
  var interpolatingMap = InterpolatingMap({
    0: 1,
    1: 2,
    2: 1,
  });

  print(interpolatingMap[-1]); // Prints: 0
  print(interpolatingMap[0]); // Prints: 1
  print(interpolatingMap[0.25]); // Prints: 1.25
  print(interpolatingMap[0.5]); // Prints: 1.5
  print(interpolatingMap[0.75]); // Prints: 1.75
  print(interpolatingMap[1]); // Prints: 2
  print(interpolatingMap[1.5]); // Prints: 1.5
  print(interpolatingMap[3]); // Prints: 0
}
