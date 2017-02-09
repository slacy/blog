Title: Avoiding accumulated error while using GPolyLine (Google Maps API)
Date: 2007-01-13 23:06
Author: slacy
Category: Geocaching, Web
Status: published

If you're using the GPolyLine() API to Google Maps, and you're using the
string encoding to store a large number of points, you have to be very
careful not to incur accumulated error as you encode the points.

The problem comes from the fact that the GPolyLine function fromEncoded
uses a special encoding that only encodes 5 digits of precision beyond
the decimal point. So, if you're not careful, those left over bits after
the 5th digit (if your source data has them) can add up to a nasty
amount of error over time. A line with only a hundred or so points won't
show much error, but when you get to thousands, it ads up pretty
quickly. You'll see this problem manifest itself as a line whose
starting position is perfect, but at the end of the line, it will be
shifted several hundred feet in some direction.

This comes from the fact that the Polyline encoding uses 5 digit
precision *delta* values to encode the difference between the previous
point and the next. Full positions are only encoded at the beginning of
each segment.

A naive algogithm, like the one below, will reproduce the error:

` Encode( RoundToFiveDigits( point[0] ) ); for i = 1..points: Encode( RoundToFiveDigits( point[i] - point[i-1] ) );`

And, if you change the code as follows, you won't get the accumulated
error:

` Encode( RoundToFiveDigits( point[0] ); for i = 1 .. points: Encode( RoundToFiveDigits( point[i] ) - RoundToFiveDigits(point[i-1]) );`

It's subtle, but it makes a *huge* difference when you're encoding
several thousand points. When I first thought that this might be the
problem, my thought was that if there was rounding error, that on
average, it should work out that the errors should all add up to zero,
with equal amounts of positive and negative error in each direction. The
flaw in this logic is that 5 digits is probably just on the edge of what
my GPS unit can distinguish, and thus, the 6th digit probably has a
higher likelihood of being one value versus another, so the start to
accumulate.
