import sys
import neuroml.v2 as nml
import Utils as u
import numpy as np
from neuroml.v2 import neuroml

class AbstractCell(nml.Standalone):
    subclass = None
    superclass = nml.Standalone
    def __init__(self, cell_id = None, neuroLexId = None, metaid = None, notes = None, annotation = None, extensiontype_ = None):
        super(AbstractCell, self).__init__(cell_id, neuroLexId, metaid, notes, annotation, extensiontype_,)
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if AbstractCell.subclass:
            return AbstractCell.subclass(*args_, **kwargs_)
        else:
            return AbstractCell(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(): return None
    get_Name = staticmethod(get_Name)

class MorrisLecarCell(nml.AbstractCell):
    subclass = None
    superclass = nml.AbstractCell
    def __init__(self, cell_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, C = None, I = None, gL = None,
                 gCa = None, gK = None, VL = None, VCa = None, VK = None, V1 = None,
                 V2 = None, V3 = None, V4 = None, phi = None, parent = None):
        super(MorrisLecarCell, self).__init__(cell_id, neuroLexId, metaid, notes, annotation,)
        self.C = nml._cast(None, C)
        self.I = nml._cast(None, I)
        self.gL = nml._cast(None, gL)
        self.gCa = nml._cast(None, gCa)
        self.gK = nml._cast(None, gK)
        self.VL = nml._cast(None, VL)
        self.VCa = nml._cast(None, VCa)
        self.VK = nml._cast(None, VK)
        self.V1 = nml._cast(None, V1)
        self.V2 = nml._cast(None, V2)
        self.V3 = nml._cast(None, V3)
        self.V4 = nml._cast(None, V4)
        self.phi = nml._cast(None, phi)
        self.parent = parent
        pass
    def factory(*args_, **kwargs_):
        if MorrisLecarCell.subclass:
            return MorrisLecarCell.subclass(*args_, **kwargs_)
        else:
            return MorrisLecarCell(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_C(self): return self.C
    def set_C(self, C): self.C = C
    def get_I(self): return self.I
    def set_I(self, I): self.I = I
    def get_gL(self): return self.gL
    def set_gL(self, gL): self.gL = gL
    def get_gCa(self): return self.gCa
    def set_gCa(self, gCa): self.gCa = gCa
    def get_gK(self): return self.gK
    def set_gK(self, gK): self.gK = gK
    def get_VCa(self): return self.VCa
    def set_VCa(self, VCa): self.VCa = VCa
    def get_VK(self): return self.VK
    def set_VK(self, VK): self.VK = VK
    def get_VL(self): return self.VL
    def set_VL(self, VL): self.VL = VL
    def get_V1(self): return self.V1
    def set_V1(self, V1): self.V1 = V1
    def get_V2(self): return self.V2
    def set_V2(self, V2): self.V2 = V2
    def get_V3(self): return self.V3
    def set_V3(self, V3): self.V3 = V3
    def get_V4(self): return self.V4
    def set_V4(self, V4): self.V4 = V4
    def get_phi(self): return self.phi
    def set_phi(self, phi): self.phi = phi
    def validate_Nml2Quantity_voltage(self, value):
        # Validate type Nml2Quantity_voltage, a restriction on xs:string.
        pass
    def validate_Nml2Quantity_capacitance(self, value):
        # Validate type Nml2Quantity_capacitance, a restriction on xs:string.
        pass
    def validate_Nml2Quantity_conductance(self, value):
        # Validate type Nml2Quantity_conductance, a restriction on xs:string.
        pass
    def export(self, outfile, level, namespace_ = '', name_ = 'MorrisLecarCell', namespacedef_ = ''):
        nml.showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_ = 'MorrisLecarCell')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            nml.showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_ = '', name_ = 'MorrisLecarCell'):
        super(MorrisLecarCell, self).exportAttributes(outfile, level, already_processed, namespace_, name_ = 'MorrisLecarCell')
        if self.C is not None and 'C' not in already_processed:
            already_processed.append('C')
            outfile.write(' C=%s' % (nml.quote_attrib(self.C),))
        if self.I is not None and 'I' not in already_processed:
            already_processed.append('I')
            outfile.write(' I=%s' % (nml.quote_attrib(self.I),))
        if self.gL is not None and 'gL' not in already_processed:
            already_processed.append('gL')
            outfile.write(' gL=%s' % (nml.quote_attrib(self.gL),))
        if self.gCa is not None and 'gCa' not in already_processed:
            already_processed.append('gCa')
            outfile.write(' gCa=%s' % (nml.quote_attrib(self.gCa),))
        if self.gK is not None and 'gK' not in already_processed:
            already_processed.append('gK')
            outfile.write(' gK=%s' % (nml.quote_attrib(self.gK),))
        if self.VCa is not None and 'VCa' not in already_processed:
            already_processed.append('VCa')
            outfile.write(' VCa=%s' % (nml.quote_attrib(self.VCa),))
        if self.VK is not None and 'VK' not in already_processed:
            already_processed.append('VK')
            outfile.write(' VK=%s' % (nml.quote_attrib(self.VK),))
        if self.VL is not None and 'VL' not in already_processed:
            already_processed.append('VL')
            outfile.write(' VL=%s' % (nml.quote_attrib(self.VL),))
        if self.V1 is not None and 'V1' not in already_processed:
            already_processed.append('V1')
            outfile.write(' V1=%s' % (nml.quote_attrib(self.V1),))
        if self.V2 is not None and 'V2' not in already_processed:
            already_processed.append('V2')
            outfile.write(' V2=%s' % (nml.quote_attrib(self.V2),))
        if self.V3 is not None and 'V3' not in already_processed:
            already_processed.append('V3')
            outfile.write(' V3=%s' % (nml.quote_attrib(self.V3),))
        if self.V4 is not None and 'V4' not in already_processed:
            already_processed.append('V4')
            outfile.write(' V4=%s' % (nml.quote_attrib(self.V4),))
        if self.phi is not None and 'phi' not in already_processed:
            already_processed.append('phi')
            outfile.write(' phi=%s' % (nml.quote_attrib(self.phi),))
    def exportChildren(self, outfile, level, namespace_ = '', name_ = 'MorrisLecarCell', fromsubclass_ = False):
        super(MorrisLecarCell, self).exportChildren(outfile, level, namespace_, name_, True)
    def hasContent_(self):
        if (
            super(MorrisLecarCell, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_ = 'MorrisLecarCell'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.C is not None and 'C' not in already_processed:
            already_processed.append('C')
            nml.showIndent(outfile, level)
            outfile.write('C = "%s",\n' % (self.C,))
        if self.I is not None and 'I' not in already_processed:
            already_processed.append('I')
            nml.showIndent(outfile, level)
            outfile.write('I = "%s",\n' % (self.I,))
        if self.gL is not None and 'gL' not in already_processed:
            already_processed.append('gL')
            nml.showIndent(outfile, level)
            outfile.write('gL = "%s",\n' % (self.gL,))
        if self.gCa is not None and 'gCa' not in already_processed:
            already_processed.append('gCa')
            nml.showIndent(outfile, level)
            outfile.write('gCa = "%s",\n' % (self.gCa,))
        if self.gK is not None and 'gK' not in already_processed:
            already_processed.append('gK')
            nml.showIndent(outfile, level)
            outfile.write('gK = "%s",\n' % (self.gK,))
        if self.VCa is not None and 'VCa' not in already_processed:
            already_processed.append('VCa')
            nml.showIndent(outfile, level)
            outfile.write('VCa = "%s",\n' % (self.VCa,))
        if self.VK is not None and 'VK' not in already_processed:
            already_processed.append('VK')
            nml.showIndent(outfile, level)
            outfile.write('VK = "%s",\n' % (self.VK,))
        if self.VL is not None and 'VL' not in already_processed:
            already_processed.append('VL')
            nml.showIndent(outfile, level)
            outfile.write('VL = "%s",\n' % (self.VL,))
        if self.V1 is not None and 'V1' not in already_processed:
            already_processed.append('V1')
            nml.showIndent(outfile, level)
            outfile.write('V1 = "%s",\n' % (self.V1,))
        if self.V2 is not None and 'V2' not in already_processed:
            already_processed.append('V2')
            nml.showIndent(outfile, level)
            outfile.write('V2 = "%s",\n' % (self.V2,))
        if self.V3 is not None and 'V3' not in already_processed:
            already_processed.append('V3')
            nml.showIndent(outfile, level)
            outfile.write('V3 = "%s",\n' % (self.V3,))
        if self.V4 is not None and 'V4' not in already_processed:
            already_processed.append('V4')
            nml.showIndent(outfile, level)
            outfile.write('V4 = "%s",\n' % (self.V4,))
        if self.phi is not None and 'phi' not in already_processed:
            already_processed.append('phi')
            nml.showIndent(outfile, level)
            outfile.write('phi = "%s",\n' % (self.phi,))

        super(MorrisLecarCell, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(MorrisLecarCell, self).exportLiteralChildren(outfile, level, name_)
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = nml.Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = nml.find_attr_value_('C', node)
        if value is not None and 'C' not in already_processed:
            already_processed.append('C')
            self.C = value
            self.validate_Nml2Quantity_capacitance(self.C)
        value = nml.find_attr_value_('I', node)
        if value is not None and 'I' not in already_processed:
            already_processed.append('I')
            self.I = value
            self.validate_Nml2Quantity_voltage(self.I)
        value = nml.find_attr_value_('gL', node)
        if value is not None and 'gL' not in already_processed:
            already_processed.append('gL')
            self.gL = value
            self.validate_Nml2Quantity_voltage(self.gL)
        value = nml.find_attr_value_('gCa', node)
        if value is not None and 'gCa' not in already_processed:
            already_processed.append('gCa')
            self.gCa = value
            self.validate_Nml2Quantity_voltage(self.gCa)
        value = nml.find_attr_value_('gK', node)
        if value is not None and 'gK' not in already_processed:
            already_processed.append('gK')
            self.gK = value
            self.validate_Nml2Quantity_voltage(self.gK)
        value = nml.find_attr_value_('VL', node)
        if value is not None and 'VL' not in already_processed:
            already_processed.append('VL')
            self.VL = value
            self.validate_Nml2Quantity_voltage(self.VL)
        value = nml.find_attr_value_('VCa', node)
        if value is not None and 'VCa' not in already_processed:
            already_processed.append('VCa')
            self.VCa = value
            self.validate_Nml2Quantity_voltage(self.VCa)
        value = nml.find_attr_value_('VK', node)
        if value is not None and 'VK' not in already_processed:
            already_processed.append('VK')
            self.VK = value
            self.validate_Nml2Quantity_voltage(self.VK)
        if value is not None and 'V1' not in already_processed:
            already_processed.append('V1')
            self.V1 = value
            self.validate_Nml2Quantity_voltage(self.V1)
        value = nml.find_attr_value_('V2', node)
        if value is not None and 'V2' not in already_processed:
            already_processed.append('V2')
            self.V2 = value
            self.validate_Nml2Quantity_voltage(self.V2)
        value = nml.find_attr_value_('V3', node)
        if value is not None and 'V3' not in already_processed:
            already_processed.append('V3')
            self.V3 = value
            self.validate_Nml2Quantity_voltage(self.V3)
        value = nml.find_attr_value_('V4', node)
        if value is not None and 'V4' not in already_processed:
            already_processed.append('V4')
            self.V4 = value
            self.validate_Nml2Quantity_voltage(self.V4)
        value = nml.find_attr_value_('phi', node)
        if value is not None and 'phi' not in already_processed:
            already_processed.append('phi')
            self.phi = value
            self.validate_Nml2Quantity_voltage(self.phi)

        super(MorrisLecarCell, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        super(MorrisLecarCell, self).buildChildren(child_, node, nodeName_, True)
    def get_PropertiesArray(self):
        return np.array([u.Units.read(self.C),
                         u.Units.read(self.I),
                         u.Units.read(self.gL),
                         u.Units.read(self.gCa),
                         u.Units.read(self.gK),
                         u.Units.read(self.VCa),
                         u.Units.read(self.VK),
                         u.Units.read(self.VL),
                         u.Units.read(self.V1),
                         u.Units.read(self.V2),
                         u.Units.read(self.V3),
                         u.Units.read(self.V4),
                         self.phi], dtype = np.float64)
    def get_Name(): return 'MorrisLecarCell'
    get_Name = staticmethod(get_Name)
    def get_Num_Parameters(): return 13
    get_Num_Parameters = staticmethod(get_Num_Parameters)

class ExpOneSynapse(nml.ExpOneSynapse):
    def __init__(self, cell_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, erev = None, gbase = None, tauDecay = None, parent = None):
        super(ExpOneSynapse, self).__init__(cell_id, neuroLexId, metaid, notes,
                                            annotation, erev, gbase, tauDecay,)
        self.parent = parent
    def factory(*args_, **kwargs_):
        if ExpOneSynapse.subclass:
            return ExpOneSynapse.subclass(*args_, **kwargs_)
        else:
            return ExpOneSynapse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PropertiesArray(self):
        return np.array([u.Units.read(self.erev),
                         u.Units.read(self.gbase),
                         u.Units.read(self.tauDecay)])
    def get_Name(): return 'ExpOneSynapse'
    get_Name = staticmethod(get_Name)

class IaFCell(nml.IaFCell):
    def __init__(self, cell_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, reset = None, C = None, thresh = None,
                 leakConductance = None, leakReversal = None, parent = None):
        super(IaFCell, self).__init__(cell_id, neuroLexId, metaid, notes,
                                      annotation, reset, C, thresh,
                                      leakConductance, leakReversal,)
        self.parent = parent
    def factory(*args_, **kwargs_):
        if IaFCell.subclass:
            return IaFCell.subclass(*args_, **kwargs_)
        else:
            return IaFCell(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PropertiesArray(self):
        return np.array([u.Units.read(self.reset),
                         u.Units.read(self.C),
                         u.Units.read(self.thresh),
                         u.Units.read(self.leakConductance),
                         u.Units.read(self.leakReversal)])
    def get_Name(): return 'IaFCell'
    get_Name = staticmethod(get_Name)
    def get_Num_Parameters(): return 5
    get_Num_Parameters = staticmethod(get_Num_Parameters)

class MorrisLecarSynapse(nml.ConductanceBasedSynapse):
    subclass = None
    superclass = nml.ConductanceBasedSynapse
    def __init__(self, cell_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, slope = None, thresh = None, power = None,
                 saturation = None, delay = None, erev = None, factor = None,
                 parent = None):
        super(MorrisLecarSynapse, self).__init__(cell_id, neuroLexId, metaid, notes,
                                                 annotation, erev,)
        self.slope = nml._cast(None, slope)
        self.thresh = nml._cast(None, thresh)
        self.power = nml._cast(None, power)
        self.saturation = nml._cast(None, saturation)
        self.delay = nml._cast(None, delay)
        self.erev = nml._cast(None, erev)
        self.factor = nml._cast(None, factor)
        self.parent = parent
    def factory(*args_, **kwargs_):
        if MorrisLecarSynapse.subclass:
            return MorrisLecarSynapse.subclass(*args_, **kwargs_)
        else:
            return MorrisLecarSynapse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_slope(self): return self.slope
    def set_slope(self, slope): self.slope = slope
    def get_thresh(self): return self.thresh
    def set_thresh(self, thresh): self.thresh = thresh
    def get_power(self): return self.power
    def set_power(self, power): self.power = power
    def get_saturation(self): return self.saturation
    def set_saturation(self, saturation): self.saturation = saturation
    def get_delay(self): return self.delay
    def set_delay(self, delay): self.delay = delay
    def get_factor(self): return self.factor
    def set_factor(self, factor): self.factor = factor
    def get_erev(self): return self.erev
    def set_erev(self, erev): self.erev = erev
    def validate_Nml2Quantity_time(self, value):
        # Validate type Nml2Quantity_time, a restriction on xs:string.
        pass
    def export(self, outfile, level, namespace_ = '', name_ = 'MorrisLecarSynapse',
               namespacedef_ = ''):
        nml.showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + \
                                   namespacedef_ or '',))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_,
                              name_ = 'MorrisLecarSynapse')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            nml.showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_ = '',
                         name_ = 'MorrisLecarSynapse'):
        super(MorrisLecarSynapse,
              self).exportAttributes(outfile, level, already_processed,
                                     namespace_, name_ = 'MorrisLecarSynapse')
        if self.slope is not None and 'slope' not in already_processed:
            already_processed.append('slope')
            outfile.write(' slope=%s' % (nml.quote_attrib(self.slope),))
        if self.thresh is not None and 'thresh' not in already_processed:
            already_processed.append('thresh')
            outfile.write(' thresh=%s' % (nml.quote_attrib(self.thresh),))
        if self.slope is not None and 'power' not in already_processed:
            already_processed.append('power')
            outfile.write(' power=%s' % (nml.quote_attrib(self.power),))
        if self.saturation is not None and 'saturation' not in already_processed:
            already_processed.append('saturation')
            outfile.write(' saturation=%s' % (nml.quote_attrib(self.saturation),))
        if self.delay is not None and 'delay' not in already_processed:
            already_processed.append('delay')
            outfile.write(' delay=%s' % (nml.quote_attrib(self.delay),))
        if self.erev is not None and 'erev' not in already_processed:
            already_processed.append('erev')
            outfile.write(' erev=%s' % (nml.quote_attrib(self.erev),))
        if self.factor is not None and 'factor' not in already_processed:
            already_processed.append('factor')
            outfile.write(' factor=%s' % (nml.quote_attrib(self.factor),))
    def exportChildren(self, outfile, level, namespace_ = '',
                       name_ = 'MorrisLecarSynapse', fromsubclass_ = False):
        super(MorrisLecarSynapse, self).exportChildren(outfile, level,
                                                       namespace_, name_, True)
    def hasContent_(self):
        if (
            super(MorrisLecarSynapse, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_ = 'MorrisLecarSynapse'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.slope is not None and 'slope' not in already_processed:
            already_processed.append('slope')
            nml.showIndent(outfile, level)
            outfile.write('slope = "%s",\n' % (self.slope,))
        if self.thresh is not None and 'thresh' not in already_processed:
            already_processed.append('thresh')
            nml.showIndent(outfile, level)
            outfile.write('thresh = "%s",\n' % (self.thresh,))
        if self.power is not None and 'power' not in already_processed:
            already_processed.append('power')
            nml.showIndent(outfile, level)
            outfile.write('power = "%s",\n' % (self.power,))
        if self.saturation is not None and 'saturation' not in already_processed:
            already_processed.append('saturation')
            nml.showIndent(outfile, level)
            outfile.write('saturation = "%s",\n' % (self.saturation,))
        if self.delay is not None and 'delay' not in already_processed:
            already_processed.append('delay')
            nml.showIndent(outfile, level)
            outfile.write('delay = "%s",\n' % (self.delay,))
        if self.erev is not None and 'erev' not in already_processed:
            already_processed.append('erev')
            nml.showIndent(outfile, level)
            outfile.write('erev = "%s",\n' % (self.erev,))
        if self.factor is not None and 'factor' not in already_processed:
            already_processed.append('factor')
            nml.showIndent(outfile, level)
            outfile.write('factor = "%s",\n' % (self.factor,))
        super(MorrisLecarSynapse, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(MorrisLecarSynapse, self).exportLiteralChildren(outfile, level, name_)
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = nml.Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = nml.find_attr_value_('slope', node)
        if value is not None and 'slope' not in already_processed:
            already_processed.append('slope')
            self.slope = value
            self.validate_Nml2Quantity_time(self.slope)
        value = nml.find_attr_value_('thresh', node)
        if value is not None and 'thresh' not in already_processed:
            already_processed.append('thresh')
            self.thresh = value
            self.validate_Nml2Quantity_time(self.thresh)
        value = nml.find_attr_value_('power', node)
        if value is not None and 'power' not in already_processed:
            already_processed.append('power')
            self.power = value
            self.validate_Nml2Quantity_time(self.power)
        value = nml.find_attr_value_('saturation', node)
        if value is not None and 'saturation' not in already_processed:
            already_processed.append('saturation')
            self.saturation = value
            self.validate_Nml2Quantity_time(self.saturation)
        value = nml.find_attr_value_('delay', node)
        if value is not None and 'delay' not in already_processed:
            already_processed.append('delay')
            self.delay = value
            self.validate_Nml2Quantity_time(self.delay)
        value = nml.find_attr_value_('factor', node)
        if value is not None and 'factor' not in already_processed:
            already_processed.append('factor')
            self.factor = value
            self.validate_Nml2Quantity_time(self.factor)
        value = nml.find_attr_value_('erev', node)
        if value is not None and 'erev' not in already_processed:
            already_processed.append('erev')
            self.erev = value
            self.validate_Nml2Quantity_time(self.erev)
        super(MorrisLecarSynapse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        super(MorrisLecarSynapse, self).buildChildren(child_, node, nodeName_, True)
        pass
    def get_PropertiesArray(self):
        return np.array([self.slope,
                         self.thresh,
                         self.power,
                         self.saturation,
                         self.delay,
                         self.erev,
                         self.factor])
    def get_Name(): return 'MorrisLecarSynapse'
    get_Name = staticmethod(get_Name)

class Layout(nml.Layout):
    def __init__(self, space = None, random = None, grid = None, unstructured = None):
        super(Layout, self).__init__(space, random, grid, unstructured,)
    def factory(*args_, **kwargs_):
        if Layout.subclass:
            return Layout.subclass(*args_, **kwargs_)
        else:
            return Layout(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PopulationSize(self):
        if self.random is not None: return self.random.get_number()
        elif self.unstructured is not None: return self.unstructured.get_number()
        elif self.grid is not None: return self.grid.get_PopulationSize()
        else: return None
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        if nodeName_ == 'grid':
            obj_ = GridLayout.factory()
            obj_.build(child_)
            self.set_grid(obj_)
        else:
            super(Layout, self).__init__(child_, node, nodeName_, fromsubclass_,)

class LpuInputIaF(IaFCell):
    def __init__(self, obj_id = None, neuroLexId = None, extensiontype_ = None):
        super(LpuInputIaF, self).__init__(obj_id, neuroLexId, extensiontype_,)
    def factory(*args_, **kwargs_):
        if LpuInputIaF.subclass:
            return LpuInputIaF.subclass(*args_, **kwargs_)
        else:
            return LpuInputIaF(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(): return 'LpuInputIaF'
    get_Name = staticmethod(get_Name)
    def get_id(self): return self.id

class LpuOutputIaF(IaFCell):
    def __init__(self, obj_id = None, neuroLexId = None, extensiontype_ = None):
        super(LpuOutputIaF, self).__init__(obj_id, neuroLexId, extensiontype_,)
    def factory(*args_, **kwargs_):
        if LpuOutputIaF.subclass:
            return LpuOutputIaF.subclass(*args_, **kwargs_)
        else:
            return LpuOutputIaF(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(): return 'LpuOutputIaF'
    get_Name = staticmethod(get_Name)
    def get_id(self): return self.id

class LpuInputMorrisLecar(MorrisLecarCell):
    def __init__(self, obj_id = None, neuroLexId = None, extensiontype_ = None):
        super(LpuInputMorrisLecar, self).__init__(obj_id, neuroLexId, extensiontype_,)
    def factory(*args_, **kwargs_):
        if LpuInputMorrisLecar.subclass:
            return LpuInputMorrisLecar.subclass(*args_, **kwargs_)
        else:
            return LpuInputMorrisLecar(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(): return 'LpuInputMorrisLecar'
    get_Name = staticmethod(get_Name)
    def get_id(self): return self.id

class LpuOutputMorrisLecar(MorrisLecarCell):
    def __init__(self, obj_id = None, neuroLexId = None, extensiontype_ = None):
        super(LpuOutputMorrisLecar, self).__init__(obj_id, neuroLexId, extensiontype_,)
    def factory(*args_, **kwargs_):
        if LpuOutputMorrisLecar.subclass:
            return LpuOutputMorrisLecar.subclass(*args_, **kwargs_)
        else:
            return LpuOutputMorrisLecar(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(): return 'LpuOutputMorrisLecar'
    get_Name = staticmethod(get_Name)
    def get_id(self): return self.id

class Population(nml.Population):
    def __init__(self, obj_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, cell = None, extracellularProperties = None,
                 component = None, network = None, size = None, layout = None,
                 instances = None, parent = None):
        super(Population, self).__init__(obj_id, neuroLexId, metaid, notes,
                                         annotation, cell,
                                         extracellularProperties, component,
                                         network, size, layout, instances,)
        self.parent = parent
    def factory(*args_, **kwargs_):
        if Population.subclass:
            return Population.subclass(*args_, **kwargs_)
        else:
            return Population(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PopulationSize(self):
        if self.size is not None: return self.size
        elif self.layout is not None: return self.layout.get_PopulationSize()
        else: return None
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        if nodeName_ == 'layout':
            obj_ = Layout.factory()
            obj_.build(child_)
            self.set_layout(obj_)
        else:
            super(Population, self).buildChildren(child_, node, nodeName_, True)

class GridLayout(nml.GridLayout):
    subclass = None
    superclass = None
    def __init__(self, zSize = None, ySize = None, xSize = None):
        super(GridLayout, self).__init__(zSize, ySize, xSize)
    def factory(*args_, **kwargs_):
        if GridLayout.subclass:
            return GridLayout.subclass(*args_, **kwargs_)
        else:
            return GridLayout(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PopulationSize(self):
        return (self.get_xSize() if self.get_xSize() is not None else 1) * (self.get_ySize() if self.get_ySize() is not None else 1) * (self.get_zSize() if self.get_zSize() is not None else 1)

class SynapticConnection(nml.SynapticConnection):
    def __init__(self, to = None, synapse = None, fromxx = None):
        super(nml.SynapticConnection, self).init(self, to = None, synapse = None, fromxx = None)
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = nml.Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = nml.find_attr_value_('to', node)
        if value is not None and 'to' not in already_processed:
            already_processed.append('to')
            self.to = value
        value = nml.find_attr_value_('synapse', node)
        if value is not None and 'synapse' not in already_processed:
            already_processed.append('synapse')
            self.synapse = value
        value = nml.find_attr_value_('from', node)
        if value is not None and 'from' not in already_processed:
            already_processed.append('from')
            self.fromxx = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        pass

class Connection(nml.Connection):
    def __init__(self, preCellId = None, postCellId = None):
        super(nml.Connection, self).__init__()
    def factory(*args_, **kwargs_):
        if Connection.subclass:
            return Connection.subclass(*args_, **kwargs_)
        else:
            return Connection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_preCellId(self): return self._preCellId
    def get_postCellId(self): return self._postCellId
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = nml.Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = nml.find_attr_value_('preCellId', node)
        if value is not None and 'preCellId' not in already_processed:
            already_processed.append('preCellId')
            self._preCellId = value
        value = nml.find_attr_value_('postCellId', node)
        if value is not None and 'postCellId' not in already_processed:
            already_processed.append('postCellId')
            self._postCellId = value

class Projection(nml.Projection):
    subclass = None
    superclass = nml.Projection
    def __init__(self, obj_id = None, neuroLexId = None, anytypeobjs_ = None,
                 synapse = None, connection = None, presynapticPopulation = None,
                 postsynapticPopulation = None, parent = None):
        super(Projection, self).__init__(obj_id, neuroLexId,)
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        if connection == None:
            self._connection = []
        else:
            self._connection = connection
        self.parent = parent
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = nml.Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def get_synapse(self): return self._synapse
    def set_synapse(self, synapse): self._synapse = synapse
    def get_connection(self): return self._connection
    def add_connection(self, value):
        self._synapse.append(value)
    def insert_space(self, index, value): self.space[index] = value
    def get_presynapticPopulation(self): return self._presynapticPopulation
    def get_postsynapticPopulation(self): return self._postsynapticPopulation
    def set_presynapticPopulation(self, value): self._presynapticPopulation = value
    def set_postsynapticPopulation(self, value): self._postsynapticPopulation = value
    def get_connectivityMatrix(self):
        # Check if target and source are valid
        if self.parent.get_PopulationById(self._presynapticPopulation) is None:
            raise IndexError('Your source population does not exist')
        if self.parent.get_PopulationById(self._postsynapticPopulation) is None:
            raise IndexError('Your target population does not exist')
        # Full connected
        if self._synapse[0].fromxx is None:
            return np.ones((self.parent.get_PopulationById(self._presynapticPopulation).get_PopulationSize(), self.parent.get_PopulationById(self._postsynapticPopulation).get_PopulationSize()), dtype = np.bool)

        # Specific connectivity
        else:
            source = self.parent.get_PopulationById(self._presynapticPopulation)[0]
            target = self.parent.get_PopulationById(self._postsynapticPopulation)[0]
            mat = np.zeros((source.get_PopulationSize(), target.get_PopulationSize()), dtype = np.bool)
            for syn in self._synapse:
                mat[u.getId(syn.fromxx), u.getId(syn.to)] = 1

        return mat
    def factory(*args_, **kwargs_):
        if Projection.subclass:
            return Projection.subclass(*args_, **kwargs_)
        else:
            return Projection(*args_, **kwargs_)
    factory = staticmethod(factory)
    def buildAttributes(self, node, attrs, already_processed):
        value = nml.find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.append('id')
            self._id = value
        value = nml.find_attr_value_('presynapticPopulation', node)
        if value is not None and 'presynapticPopulation' not in already_processed:
            already_processed.append('presynapticPopulation')
            self._presynapticPopulation = value
        value = nml.find_attr_value_('postsynapticPopulation', node)
        if value is not None and 'postsynapticPopulation' not in already_processed:
            already_processed.append('postsynapticPopulation')
            self._postsynapticPopulation = value
        value = nml.find_attr_value_('synapse', node)
        if value is not None and 'synapse' not in already_processed:
            already_processed.append('synapse')
            self._synapse = value
        super(Projection, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        if nodeName_ == 'connection':
            obj_ = Connection.factory()
            obj_.build(child_)
            self._connection.append(obj_)
        else:
            super(Projection, self).buildChildren(child_, node, nodeName_, True)
    def isFullConnected(self):
        return not bool(len(self._connection))

class Network(nml.Network):
    def __init__(self, obj_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, space = None, region = None, population = None,
                 cellSet = None, projection = None, synapticConnection = None,
                 connection = None, explicitInput = None, parent = None):
        super(Network, self).__init__(obj_id, neuroLexId, metaid, notes,
                                      annotation, space, region, population,
                                      cellSet, projection, synapticConnection,
                                      connection, explicitInput,)
        self.parent = parent
    def factory(*args_, **kwargs_):
        if Network.subclass:
            return Network.subclass(*args_, **kwargs_)
        else:
            return Network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        if nodeName_ == 'space':
            obj_ = nml.Space.factory()
            obj_.build(child_)
            self.space.append(obj_)
        elif nodeName_ == 'region':
            obj_ = nml.Region.factory()
            obj_.build(child_)
            self.region.append(obj_)
        elif nodeName_ == 'population':
            obj_ = Population.factory()
            obj_.parent = self
            obj_.build(child_)
            self.population.append(obj_)
        elif nodeName_ == 'cellSet':
            obj_ = nml.CellSet.factory()
            obj_.build(child_)
            self.cellSet.append(obj_)
        elif nodeName_ == 'projection':
            obj_ = Projection.factory()
            obj_.parent = self
            obj_.build(child_)
            self.projection.append(obj_)
        elif nodeName_ == '_synapse':
            obj_ = SynapticConnection.factory()
            obj_.build(child_)
            self._synapse.append(obj_)
        elif nodeName_ == 'connection':
            obj_ = nml.Connection.factory()
            obj_.build(child_)
            self.connection.append(obj_)
        elif nodeName_ == 'explicitInput':
            obj_ = nml.ExplicitInput.factory()
            obj_.build(child_)
            self.explicitInput.append(obj_)
        else:
            super(Network, self).buildChildren(child_, node, nodeName_, True)
    def get_PopulationById(self, pop_id):
        if self.get_population() is None: return None
        else:
            try:
                if pop_id.find('/') <> -1:
                    return self.parent.get_ComponentById(self.get_PopulationById(u.getName(u.removeLowerLevel(pop_id)))[0].network).get_NetworkById(self.get_PopulationById(u.getName(u.removeLowerLevel(pop_id)))[0].network).get_PopulationById(u.getName(u.removeUpperLevel(pop_id)))
                for i, p in enumerate(self.get_population()):
                    if p.id == pop_id:
                        return p, i
            except Exception as e:
                raise Exception('CircuitML.get_PopulationById: Error trying to obtain population: ' + pop_id + '\n\tInner exception: ' + e.args[0])
        return None
    def get_CellNumber(self):
        temp = 0
        for pop in self.get_population():
            temp += pop.get_PopulationSize()
        return temp

class LpuSpecification(nml.neuroml):
    def __init__(self, obj_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, include = None, extracellularProperties = None,
                 intracellularProperties = None, morphology = None,
                 ionChannel = None, expOneSynapse = None, expTwoSynapse = None,
                 nmdaSynapse = None, stpSynapse = None, biophysicalProperties = None,
                 cell = None, abstractCell = None, iafTauCell = None, iafCell = None,
                 izhikevichCell = None, adExIaFCell = None, pulseGenerator = None,
                 network = None, morrisLecarSynapse = None,
                 morrisLecarCell = None, lpuInputsIaF = None, lpuOutputsIaF = None,
                 lpuInputsMorrisLecar = None, lpuOutputsMorrisLecar = None):
        super(LpuSpecification, self).__init__(obj_id, neuroLexId, metaid, notes, annotation,)
        if morrisLecarCell is None:
            self.morrisLecarCell = []
        else:
            self.morrisLecarCell = morrisLecarCell
        if morrisLecarSynapse is None:
            self.morrisLecarSynapse = []
        else:
            self.morrisLecarSynapse = morrisLecarSynapse
        if lpuInputsIaF is None:
            self.lpuInputsIaF = []
        else:
            self.lpuInputsIaF = lpuInputsIaF
        if lpuOutputsIaF is None:
            self.lpuOutputsIaF = []
        else:
            self.lpuOutputsIaF = lpuOutputsIaF
        if lpuInputsMorrisLecar is None:
            self.lpuInputMorrisLecar = []
        else:
            self.lpuInputMorrisLecar = lpuInputsMorrisLecar
        if lpuOutputsMorrisLecar is None:
            self.lpuOutputMorrisLecar = []
        else:
            self.lpuOutputMorrisLecar = lpuOutputsMorrisLecar
        if include is None:
            self.include = {}
        else:
            self.include = include
        self.paths = None
    def factory(*args_, **kwargs_):
        if LpuSpecification.subclass:
            return LpuSpecification.subclass(*args_, **kwargs_)
        else:
            return LpuSpecification(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_CellNumber(self):
        temp = 0
        for net in self.get_network():
            temp += net.get_CellNumber()
        return temp
    def get_LpuInput(self): return self.lpuInput
    def get_LpuOnput(self): return self.lpuOnput
    def get_external(self): return self.external
    def set_external(self, external):
        self.external = external
    def add_external(self, value): self.external.append(value)
    def insert_external(self, index, value):
        self.external[index] = value
    def get_morrisLecarSynapse(self): return self.morrisLecarSynapse
    def set_morrisLecarSynapse(self, morrisLecarSynapse):
        self.morrisLecarSynapse = morrisLecarSynapse
    def add_morrisLecarSynapse(self, value): self.morrisLecarSynapse.append(value)
    def get_iafCellById(self, obj_id):
        try:
            if self.get_iafCell() is None: return None
            else:
                for c in self.get_iafCell():
                    if c.id == obj_id: return c
        except Exception as e:
            raise Exception('CircuitML.get_iafCellById: Error trying to obtain component: ' + obj_id + '\n\tInner exception: ' + e.args[0])
        return None
    def get_morrisLecarCellById(self, obj_id):
        try:
            if self.get_morrisLecarCell() is None: return None
            else:
                for c in self.get_morrisLecarCell():
                    if c.id == obj_id: return c
        except Exception as e:
            raise Exception('CircuitML.get_morrisLecarCellById: Error trying to obtain component: ' + obj_id + '\n\tInner exception: ' + e.args[0])
        return None
    def get_CellById(self, obj_id):
        try:
            cell = self.get_iafCellById(obj_id)
            if cell is None: cell = self.get_morrisLecarCellById(obj_id)
            if cell is None:
                for inc in self.include:
                    cell = self.include[inc].get_CellById(obj_id[(obj_id.find('/') + 1):])[0]
            if cell is None: return None, ''
        except Exception as e:
            raise Exception('CircuitML.get_CellById: Error trying to obtain component: ' + obj_id + '\n\tInner exception: ' + e.args[0])
        return cell, cell.get_Name()
    def get_ComponentById(self, obj_id):
        try:
            x = self.get_AllComponentsArr()
            for comp_arr in x:
                for comp in comp_arr:
                    if type(comp_arr) == dict:
                        if comp == obj_id: return comp_arr[obj_id]
                    else:
                        if comp.get_id() == obj_id: return comp
        except Exception as e:
            raise Exception('CircuitML.get_ComponentById: Error trying to obtain component: ' + obj_id + '\n\tInner exception: ' + e.args[0])
    # Same function as above, but in another form - to remove one in the future
    def get_ComponentByPath(self, path):
        try:
            doc = self
            if path.find('/') <> -1:
                doc = self._get_XmlDoc(path, self)
            components = doc.get_AllComponentsArr()
            name = path[path.rfind('/') + 1:]
            for comp_arr in components:
                for comp in comp_arr:
                    if type(comp_arr) <> dict:
                        if comp.get_id() == name:
                            return comp
                    else:
                        return comp
        except Exception as e:
            raise Exception('CircuitML.get_ComponentByPath: Error trying to obtain component from path {0}\n\tInner exception: '.format(path) + e.args[0])
    def _get_XmlDoc(self, path, xmlDoc):
        if path.find('/') <> -1:
            for k in xmlDoc.include:
                return self._get_XmlDoc(u.removeLowerLevel(path), xmlDoc.include[k])
        return xmlDoc
    def get_morrisLecarSynapseById(self, obj_id):
        if self.get_morrisLecarSynapse() is None: return None
        else:
            for s in self.get_morrisLecarCell():
                if s.id == obj_id: return s
        return None
    def get_expOneSynapseById(self, obj_id):
        if self.get_expOneSynapse() is None: return None
        else:
            for s in self.get_expOneSynapse():
                if s.id == obj_id: return s
        return None
    def get_NetworkById(self, obj_id):
        if self.get_network() is None: return None
        else:
            for n in self.get_network():
                if n.id == obj_id: return n
        return None
    def insert_morrisLecarSynapse(self, index, value):
        self.morrisLecarSynapse[index] = value
    def get_morrisLecarCell(self): return self.morrisLecarCell
    def set_morrisLecarCell(self, morrisLecarCell):
        self.morrisLecarCell = morrisLecarCell
    def add_morrisLecarCell(self, value): self.morrisLecarCell.append(value)
    def insert_morrisLecarCell(self, index, value):
        self.morrisLecarCell[index] = value
    def exportChildren(self, outfile, level, namespace_ = '', name_ = 'neuroml',
                       fromsubclass_ = False):
        nml.Annotation.exportChildren(self, outfile, level, namespace_, name_,
                           fromsubclass_)
        for morrisLecarCell_ in self.morrisLecarCell:
            morrisLecarCell_.export(outfile, level, namespace_,
                                    name_ = 'morrisLecarCell')
        for morrisLecarSynapse_ in self.morrisLecarSynapse:
            morrisLecarSynapse_.export(outfile, level, namespace_,
                                    name_ = 'morrisLecarSynapse')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        if nodeName_ == 'morrisLecarCell':
            try:
                obj_ = MorrisLecarCell.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.morrisLecarCell.append(obj_)
        elif nodeName_ == 'morrisLecarSynapse':
            try:
                obj_ = MorrisLecarSynapse.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.morrisLecarSynapse.append(obj_)
        elif nodeName_ == 'Include':
            try:
                obj_ = u.parse(child_.get('href'))
            except:
                raise
            self.include[obj_.id] = obj_
        elif nodeName_ == 'expOneSynapse':
            try:
                obj_ = ExpOneSynapse.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.expOneSynapse.append(obj_)
        elif nodeName_ == 'iafCell':
            try:
                obj_ = IaFCell.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.iafCell.append(obj_)
        elif nodeName_ == 'network':
            try:
                obj_ = Network.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.network.append(obj_)
        elif nodeName_ == 'lpuInputIaF':
            try:
                obj_ = LpuInputIaF.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.lpuInputsIaF.append(obj_)
        elif nodeName_ == 'lpuOutputIaF':
            try:
                obj_ = LpuOutputIaF.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.lpuOutputsIaF.append(obj_)
        elif nodeName_ == 'lpuInputMorrisLecar':
            try:
                obj_ = LpuInputMorrisLecar.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.lpuInputMorrisLecar.append(obj_)
        elif nodeName_ == 'lpuOutputMorrisLecar':
            try:
                obj_ = LpuOutputMorrisLecar.factory()
                obj_.parent = self
                obj_.build(child_)
            except:
                raise
            self.lpuOutputMorrisLecar.append(obj_)
        else:
            try:
                super(LpuSpecification, self).buildChildren(child_, node, nodeName_, True)
            except:
                raise
    def hasContent_(self):
        if (nml.neuroml.hasContent_(self) or
            self.external or
            self.morrisLecarCell or
            self.morrisLecarSynapse):
            return True
        else:
            return False
    def get_Name(): return 'LpuSpecification'
    get_Name = staticmethod(get_Name)
    def get_AllComponentsDict(self, neuromlDoc):
        all_comp = {}
        for att_name in neuromlDoc.__dict__:
            att = neuromlDoc.__getattribute__(att_name)
            if type(att) == list and \
                len(att) > 0 and \
                u.isComponent(att[0]):
                all_comp[att[0].get_Name()] = att
        # Add includes
        inc = neuromlDoc.__dict__['include']
        if len(inc) > 0:
            for att in inc:
                all_comp[inc[att].get_Name() + '/' + inc[att].get_id()] = [inc[att]]
                x = inc[att].get_AllComponentsDict(inc[att])
                for k in x:
                    for e in x[k]:
                        e.id = att + '/' + e.id
                all_comp.update(x)
            inc[att].get_id()
        return all_comp
    def get_AllComponentsArr(self):
        try:
            all_comp = []
            for att_name in self.__dict__:
                att = self.__getattribute__(att_name)
                if (type(att) == list and \
                    len(att) > 0 and \
                    u.isComponent(att[0])) or \
                    (att_name == 'include' and len(att)):
                    all_comp += [att]
        except Exception as e:
            raise Exception('CircuitML.get_AllComponentsArr: Error reading the attribute: ' + att_name + ' from ' + self.id + '\n\tInner exception: ' + e.args[0])
        return all_comp
    def get_Paths(self, resetCache = False, innerDoc = None):
        if resetCache: self.paths = None
        try:
            if self.paths is None:
                # Make all paths
                self._getComponents()
                # Calculate offset
                self._calculateOffset()
                return self.paths
            else:
                return self.paths
        except Exception as e:
            raise Exception('CircuitML.get_Paths: Error while creating the paths.\n\tInner exception: ' + e.args[0])
    def _getComponents(self):
        """
        This method is VERY poorly implemented - I just didn't have time to throw it way.
        """
        try:
            # Get components
            self.all_comp = self.get_AllComponentsArr()
            # Create cells dict with name and id
            cells = self._createDict()
            # Create type dict (list_cells) with types as keys
            list_cells = self._puttypes()
        except Exception as e:
            raise Exception('CircuitML._getComponents: Error getting components.\n\tInner exception: ' + e.args[0])
        # Populate type dict (list_cells) with paths
        try:
            for net in self.get_network():
#                temp_offset = np.zeros(len(net.get_population()))
                try:
                    for pop in net.get_population():
                        if pop.component is not None:
                            list_cells[cells[pop.component]][net.id + '/' + pop.id + '/' + pop.component] = pop.get_PopulationSize()
                        else:
                            list_cells[cells[pop.network]][net.id + '/' + pop.id + '/' + pop.network] = pop.get_PopulationSize()
                except Exception as e:
                    raise Exception('CircuitML._getComponents: Error in population ' + pop.id + '.\n\tInner exception: ' + e.args[0])
        except Exception as e:
            raise Exception('CircuitML._getComponents: Error in network ' + net.id + '.\n\tInner exception: ' + e.args[0])
        # Process includes
        try:
            keys = list_cells.keys()
            for str_name in keys:
                if str_name.split('/')[0] == 'LpuSpecification':
                    for pop in list_cells[str_name]:
                            u.idxDict(list_cells, str_name, pop, self.include[str_name.split('/')[1]].get_Paths(), list_cells[str_name][pop])
                    del list_cells[str_name]
        except Exception as e:
            raise Exception('CircuitML._getComponents: Error processing included file ' + str_name + '\n\tInner exception: ' + e.args[0])
        self.paths = list_cells
    def _createDict(self):
        cells = {}
        try:
            for list_com in self.all_comp:
                if type(list_com) == dict:
                    for cell in list_com:
                        cells[list_com[cell].get_id()] = list_com[cell].get_Name() + '/' + list_com[cell].get_id()
                else:
                    for cell in list_com:
                        if issubclass(cell.__class__, nml.AbstractCell):
                            cells[cell.get_id()] = cell.get_Name()
        except Exception as e:
            raise Exception('CircuitML._createDict: Error reading cell: ' + cell.id + ' from ' + self.id + '\n\tInner exception: ' + e.args[0])
        return cells
    def _puttypes(self):
        list_cells = {}
        try:
            for c in self.all_comp:
                if type(c) == dict:
                    for k in c:
                        list_cells[c[k].get_Name() + '/' + c[k].get_id()] = {}
                else:
                    if issubclass(c[0].__class__, nml.AbstractCell):
                        list_cells[c[0].get_Name()] = {}
        except Exception as e:
            raise Exception('CircuitML._puttypes: Error creating type for: ' + str(c) + ' in ' + self.id + '\n\tInner exception: ' + e.args[0])
        return list_cells
    def _calculateOffset(self):
        offset = range(len(self.paths))
        try:
            for i, c in enumerate(self.paths.values()):
                offset[i] = c.values()
            for v in offset:
                last = 0
                cur = 0
                for j, e in enumerate(v):
                    last += v[j]
                    v[j] = cur
                    cur = last
        except Exception as e:
            raise Exception('CircuitML._calculateOffset: Error generating the offset array for the elements ' + str(c) + '\n\tInner exception: ' + e.args[0])
        self.offset = {}
        for i, c in enumerate(self.paths):
            for j, k in enumerate(self.paths[c]):
                # self.offset[u.concatWithChar(k.split('/')[:-1], '/')] = offset[i][j]
                self.offset[u.removeLowerLevel(k)] = offset[i][j]

class Include(LpuSpecification):
    def __init__(self, obj_id = None, neuroLexId = None, metaid = None, notes = None,
                 annotation = None, include = None, extracellularProperties = None,
                 intracellularProperties = None, morphology = None,
                 ionChannel = None, expOneSynapse = None, expTwoSynapse = None,
                 nmdaSynapse = None, stpSynapse = None, biophysicalProperties = None,
                 cell = None, abstractCell = None, iafTauCell = None, iafCell = None,
                 izhikevichCell = None, adExIaFCell = None, pulseGenerator = None,
                 network = None, morrisLecarSynapse = None, morrisLecarCell = None):
        super(Include, self).__init__(obj_id, neuroLexId, metaid, notes, annotation,)
        if morrisLecarCell is None:
            self.morrisLecarCell = []
        else:
            self.morrisLecarCell = morrisLecarCell
        if morrisLecarSynapse is None:
            self.morrisLecarSynapse = []
        else:
            self.morrisLecarSynapse = morrisLecarSynapse
    def factory(*args_, **kwargs_):
        if Include.subclass:
            return Include.subclass(*args_, **kwargs_)
        else:
            return Include(*args_, **kwargs_)
    factory = staticmethod(factory)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_ = False):
        super(Include, self).buildChildren(child_, node, nodeName_, True)

nml.__all__ += [
                "LpuSpecification",
                "MorrisLecarCell",
                "MorrisLecarSynapse",
                "Include",
                "LpuInputIaF",
                "LpuOutputIaF",
                "LpuInputMorrisLecar",
                "LpuOutputMorrisLecar",
                ]
