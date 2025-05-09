//+
SetFactory("OpenCASCADE");
Rectangle(1) = {0, 0, 0, 1, 0.5, 0};
//+
Physical Curve("bnd", 5) = {3, 4, 1, 2};
//+
Physical Surface("domain", 6) = {1};
