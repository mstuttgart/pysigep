# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################

from pysigep.rastreamento.consulta_rastreamento import RequestRastreamento
from pysigep.rastreamento.consulta_rastreamento import ResponseRastreamento

from unittest import TestCase


class TestConsultaRastreamento(TestCase):

    def test_get_data(self):
        req = RequestRastreamento('ECT', 'SRO',
                                  RequestRastreamento.TIPO_LISTA_DE_OBJETOS,
                                  RequestRastreamento.ULTIMO_RESULTADO,
                                  ['PJ472895891BR', 'PJ382325976BR'])

        params = {
            'Usuario': 'ECT',
            'Senha': 'SRO',
            'Tipo': 'L',
            'Resultado': 'U',
            'Objetos': 'PJ472895891BRPJ382325976BR',
        }

        self.assertDictEqual(params, req.get_data())


class TestResponseRastreamento(TestCase):

    def test_parse_xml(self):
        xml = '''<?xml version=\"1.0\" encoding=\"iso-8859-1\" ?>
<sroxml>
   <versao>1.0</versao>
   <qtd>2</qtd>
   <TipoPesquisa>Lista de Objetos</TipoPesquisa>
   <TipoResultado>Último evento</TipoResultado>
     <objeto>
       <numero>PJ382325976BR</numero>
       <evento>
          <tipo>BDE</tipo>
          <status>01</status>
          <data>03/02/2016</data>
          <hora>17:57</hora>
          <descricao>Objeto entregue ao destinatário</descricao>
          <recebedor>recebedor</recebedor>
          <documento>doc</documento>
          <comentario>comentario</comentario>
          <local>CDD ITAJUBA</local>
          <codigo>37500971</codigo>
          <cidade>Itajuba</cidade>
          <uf>MG</uf>
          <sto>00008887</sto>
      </evento>
     </objeto>
     <objeto>
       <numero>PJ472895891BR</numero>
       <evento>
          <tipo>BDE</tipo>
          <status>01</status>
          <data>03/03/2016</data>
          <hora>18:11</hora>
          <descricao>Objeto entregue ao destinatário</descricao>
          <recebedor>recebedor</recebedor>
          <documento>doc</documento>
          <comentario>comentario</comentario>
          <local>CDD ITAJUBA</local>
          <codigo>37500971</codigo>
          <cidade>Itajuba</cidade>
          <uf>MG</uf>
          <sto>00008887</sto>
      </evento>
     </objeto>
</sroxml>
'''
        resp = ResponseRastreamento()
        resp._parse_xml(xml)

        self.assertEqual(resp.resposta['versao'], '1.0')
        self.assertEqual(resp.resposta['qtd'], '2')
        self.assertEqual(resp.resposta['tipo_pesquisa'], 'Lista de Objetos')
        self.assertEqual(resp.resposta['tipo_resultado'], u'Último evento')

        # Primeiro evendo
        obj = resp.resposta['objetos']['PJ382325976BR'][0]

        self.assertEqual(obj['tipo'], 'BDE')
        self.assertEqual(obj['status'], '01')
        self.assertEqual(obj['data'], '03/02/2016')
        self.assertEqual(obj['hora'], '17:57')
        self.assertEqual(obj['descricao'], u'Objeto entregue ao destinatário')
        self.assertEqual(obj['recebedor'], 'recebedor')
        self.assertEqual(obj['documento'], 'doc')
        self.assertEqual(obj['comentario'], 'comentario')
        self.assertEqual(obj['local'], 'CDD ITAJUBA')
        self.assertEqual(obj['codigo'], '37500971')
        self.assertEqual(obj['cidade'], 'Itajuba')
        self.assertEqual(obj['uf'], 'MG')
