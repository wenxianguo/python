#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tallhigh = float(input('请输入身高'));
weight = float(input('请输入体重'));

BMI = (weight/tallhigh) * (weight/tallhigh);

if BMI < 18.5:
    print('过轻');
elif BMI <25:
    print('正常');
elif BMI <28:
    print('过重');
elif BMI <32:
    print('肥胖');
else:
    print('验证肥胖');

